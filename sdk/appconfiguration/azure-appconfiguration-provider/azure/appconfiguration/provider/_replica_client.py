# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------
import logging
import json
import time
import random
from dataclasses import dataclass
from typing import Tuple, Union, Dict, List, Any, Optional, Mapping
from azure.core import MatchConditions
from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError
from azure.core.credentials import TokenCredential
from azure.appconfiguration import (  # type:ignore # pylint:disable=no-name-in-module
    ConfigurationSetting,
    AzureAppConfigurationClient,
    FeatureFlagConfigurationSetting,
)
from ._models import SettingSelector
from ._constants import FEATURE_FLAG_PREFIX


@dataclass
class ReplicaClient:
    endpoint: str
    _client: AzureAppConfigurationClient
    backoff_end_time: float = 0
    failed_attempts: int = 0

    @classmethod
    def from_credential(
        cls,
        endpoint: str,
        credential: TokenCredential,
        user_agent: str,
        retry_total: int,
        retry_backoff_max: int,
        **kwargs
    ) -> "ReplicaClient":
        """
        Creates a new instance of the ReplicaClient class, using the provided credential to authenticate requests.

        :param str endpoint: The endpoint of the App Configuration store
        :param TokenCredential credential: The credential to use for authentication
        :param str user_agent: The user agent string to use for the request
        :param int retry_total: The total number of retries to allow for requests
        :param int retry_backoff_max: The maximum backoff time for retries
        :return: A new instance of the ReplicaClient class
        :rtype: ReplicaClient
        """
        return cls(
            endpoint,
            AzureAppConfigurationClient(
                endpoint,
                credential,
                user_agent=user_agent,
                retry_total=retry_total,
                retry_backoff_max=retry_backoff_max,
                **kwargs
            ),
        )

    @classmethod
    def from_connection_string(
        cls, endpoint: str, connection_string: str, user_agent: str, retry_total: int, retry_backoff_max: int, **kwargs
    ) -> "ReplicaClient":
        """
        Creates a new instance of the ReplicaClient class, using the provided connection string to authenticate
        requests.

        :param str endpoint: The endpoint of the App Configuration store
        :param str connection_string: The connection string to use for authentication
        :param str user_agent: The user agent string to use for the request
        :param int retry_total: The total number of retries to allow for requests
        :param int retry_backoff_max: The maximum backoff time for retries
        :return: A new instance of the ReplicaClient class
        :rtype: ReplicaClient
        """
        return cls(
            endpoint,
            AzureAppConfigurationClient.from_connection_string(
                connection_string,
                user_agent=user_agent,
                retry_total=retry_total,
                retry_backoff_max=retry_backoff_max,
                **kwargs
            ),
        )

    def _check_configuration_setting(
        self, key: str, label: str, etag: Optional[str], headers: Dict[str, str], **kwargs
    ) -> Tuple[bool, Union[ConfigurationSetting, None]]:
        """
        Checks if the configuration setting have been updated since the last refresh.

        :param str key: key to check for chances
        :param str label: label to check for changes
        :param str etag: etag to check for changes
        :param Mapping[str, str] headers: headers to use for the request
        :return: A tuple with the first item being true/false if a change is detected. The second item is the updated
        value if a change was detected.
        :rtype: Tuple[bool, Union[ConfigurationSetting, None]]
        """
        try:
            updated_sentinel = self._client.get_configuration_setting(  # type: ignore
                key=key, label=label, etag=etag, match_condition=MatchConditions.IfModified, headers=headers, **kwargs
            )
            if updated_sentinel is not None:
                logging.debug(
                    "Refresh all triggered by key: %s label %s.",
                    key,
                    label,
                )
                return True, updated_sentinel
        except HttpResponseError as e:
            if e.status_code == 404:
                if etag is not None:
                    # If the sentinel is not found, it means the key/label was deleted, so we should refresh
                    logging.debug("Refresh all triggered by key: %s label %s.", key, label)
                    return True, None
            else:
                raise e
        return False, None

    @distributed_trace
    def load_configuration_settings(
        self, selects: List[SettingSelector], refresh_on: Dict[Tuple[str, str], str], **kwargs
    ) -> Tuple[List[ConfigurationSetting], Dict[Tuple[str, str], str]]:
        configuration_settings = []
        sentinel_keys = kwargs.pop("sentinel_keys", refresh_on)
        for select in selects:
            configurations = self._client.list_configuration_settings(
                key_filter=select.key_filter, label_filter=select.label_filter, **kwargs
            )
            for config in configurations:
                if isinstance(config, FeatureFlagConfigurationSetting):
                    # Feature flags are ignored when loaded by Selects, as they are selected from
                    # `feature_flag_selectors`
                    pass
                configuration_settings.append(config)
                # Every time we run load_all, we should update the etag of our refresh sentinels
                # so they stay up-to-date.
                # Sentinel keys will have unprocessed key names, so we need to use the original key.
                if (config.key, config.label) in refresh_on:
                    sentinel_keys[(config.key, config.label)] = config.etag
        return configuration_settings, sentinel_keys

    @distributed_trace
    def load_feature_flags(
        self, feature_flag_selectors: List[SettingSelector], feature_flag_refresh_enabled: bool, **kwargs
    ) -> Tuple[List[FeatureFlagConfigurationSetting], Dict[Tuple[str, str], str]]:
        feature_flag_sentinel_keys = {}
        loaded_feature_flags = []
        # Needs to be removed unknown keyword argument for list_configuration_settings
        kwargs.pop("sentinel_keys", None)
        for select in feature_flag_selectors:
            feature_flags = self._client.list_configuration_settings(
                key_filter=FEATURE_FLAG_PREFIX + select.key_filter, label_filter=select.label_filter, **kwargs
            )
            for feature_flag in feature_flags:
                loaded_feature_flags.append(json.loads(feature_flag.value))

                if feature_flag_refresh_enabled:
                    feature_flag_sentinel_keys[(feature_flag.key, feature_flag.label)] = feature_flag.etag
        return loaded_feature_flags, feature_flag_sentinel_keys

    @distributed_trace
    def refresh_configuration_settings(
        self, selects: List[SettingSelector], refresh_on: Dict[Tuple[str, str], str], headers: Dict[str, str], **kwargs
    ) -> Tuple[bool, Dict[Tuple[str, str], str], List[Any]]:
        """
        Gets the refreshed configuration settings if they have changed.

        :param List[SettingSelector] selects: The selectors to use to load configuration settings
        :param List[SettingSelector] refresh_on: The configuration settings to check for changes
        :param Mapping[str, str] headers: The headers to use for the request

        :return: A tuple with the first item being true/false if a change is detected. The second item is the updated
        value of the configuration sentinel keys. The third item is the updated configuration settings.
        :rtype: Tuple[bool, Union[Dict[Tuple[str, str], str], None], Union[List[ConfigurationSetting], None]]
        """
        need_refresh = False
        updated_sentinel_keys = dict(refresh_on)
        for (key, label), etag in updated_sentinel_keys.items():
            changed, updated_sentinel = self._check_configuration_setting(
                key=key, label=label, etag=etag, headers=headers, **kwargs
            )
            if changed:
                need_refresh = True
            if updated_sentinel is not None:
                updated_sentinel_keys[(key, label)] = updated_sentinel.etag
        # Need to only update once, no matter how many sentinels are updated
        if need_refresh:
            configuration_settings, sentinel_keys = self.load_configuration_settings(selects, refresh_on, **kwargs)
            return True, sentinel_keys, configuration_settings
        return False, refresh_on, []

    @distributed_trace
    def refresh_feature_flags(
        self,
        refresh_on: Mapping[Tuple[str, str], Optional[str]],
        feature_flag_selectors: List[SettingSelector],
        headers: Dict[str, str],
        **kwargs
    ) -> Tuple[bool, Optional[Dict[Tuple[str, str], str]], Optional[List[Any]]]:
        """
        Gets the refreshed feature flags if they have changed.

        :param Mapping[Tuple[str, str], Optional[str]] refresh_on: The feature flags to check for changes
        :param List[SettingSelector] feature_flag_selectors: The selectors to use to load feature flags
        :param Mapping[str, str] headers: The headers to use for the request

        :return: A tuple with the first item being true/false if a change is detected. The second item is the updated
        value of the feature flag sentinel keys. The third item is the updated feature flags.
        :rtype: Tuple[bool, Union[Dict[Tuple[str, str], str], None], Union[List[Dict[str, str]], None]]
        """
        feature_flag_sentinel_keys: Mapping[Tuple[str, str], Optional[str]] = dict(refresh_on)
        for (key, label), etag in feature_flag_sentinel_keys.items():
            changed = self._check_configuration_setting(key=key, label=label, etag=etag, headers=headers, **kwargs)
            if changed:
                feature_flags, feature_flag_sentinel_keys = self.load_feature_flags(
                    feature_flag_selectors, True, **kwargs
                )
                return True, feature_flag_sentinel_keys, feature_flags
        return False, None, None

    @distributed_trace
    def get_configuration_setting(self, key: str, label: str, **kwargs) -> ConfigurationSetting:
        """
        Gets a configuration setting from the replica client.

        :param str key: The key of the configuration setting
        :param str label: The label of the configuration setting
        :return: The configuration setting
        :rtype: ConfigurationSetting
        """
        return self._client.get_configuration_setting(key=key, label=label, **kwargs)

    def close(self) -> None:
        """
        Closes the connection to Azure App Configuration.
        """
        self._client.close()

    def __enter__(self):
        self._client.__enter__()
        return self

    def __exit__(self, *args):
        self._client.__exit__(*args)


class ReplicaClientManager:
    def __init__(self, min_backoff_sec: int, max_backoff_sec: int):
        self._replica_clients: List[ReplicaClient] = []
        self._min_backoff_sec = min_backoff_sec
        self._max_backoff_sec = max_backoff_sec

    def set_clients(self, replica_clients: List[ReplicaClient]):
        self._replica_clients.clear()
        self._replica_clients.extend(replica_clients)

    def get_active_clients(self):
        active_clients = []
        for client in self._replica_clients:
            if client.backoff_end_time <= (time.time() * 1000):
                active_clients.append(client)
        return active_clients

    def backoff(self, client: ReplicaClient):
        client.failed_attempts += 1
        backoff_time = self._calculate_backoff(client.failed_attempts)
        client.backoff_end_time = (time.time() * 1000) + backoff_time

    def get_client_count(self):
        return len(self._replica_clients)

    def _calculate_backoff(self, attempts: int) -> float:
        max_attempts = 63
        ms_per_second = 1000  # 1 Second in milliseconds

        min_backoff_milliseconds = self._min_backoff_sec * ms_per_second
        max_backoff_milliseconds = self._max_backoff_sec * ms_per_second

        if self._max_backoff_sec <= self._min_backoff_sec:
            return min_backoff_milliseconds

        calculated_milliseconds = max(1, min_backoff_milliseconds) * (1 << min(attempts, max_attempts))

        if calculated_milliseconds > max_backoff_milliseconds or calculated_milliseconds <= 0:
            calculated_milliseconds = max_backoff_milliseconds

        return min_backoff_milliseconds + (
            random.uniform(0.0, 1.0) * (calculated_milliseconds - min_backoff_milliseconds)
        )

    def close(self):
        for client in self._replica_clients:
            client.close()

    def __enter__(self):
        for client in self._replica_clients:
            client.__enter__()
        return self

    def __exit__(self, *args):
        for client in self._replica_clients:
            client.__exit__(*args)
