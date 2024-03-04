# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CallConnectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the call connection."""

    UNKNOWN = "unknown"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    TRANSFERRING = "transferring"
    TRANSFER_ACCEPTED = "transferAccepted"
    DISCONNECTING = "disconnecting"
    DISCONNECTED = "disconnected"


class CallLocatorKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The call locator kind."""

    GROUP_CALL_LOCATOR = "groupCallLocator"
    SERVER_CALL_LOCATOR = "serverCallLocator"


class CallRejectReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rejection reason."""

    NONE = "none"
    BUSY = "busy"
    FORBIDDEN = "forbidden"


class CommunicationCloudEnvironmentModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The cloud that the identifier belongs to."""

    PUBLIC = "public"
    DOD = "dod"
    GCCH = "gcch"


class CommunicationIdentifierModelKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identifier kind, for example 'communicationUser' or 'phoneNumber'."""

    UNKNOWN = "unknown"
    COMMUNICATION_USER = "communicationUser"
    PHONE_NUMBER = "phoneNumber"
    MICROSOFT_TEAMS_USER = "microsoftTeamsUser"
    MICROSOFT_TEAMS_APP = "microsoftTeamsApp"


class DialogInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of the dialog."""

    POWER_VIRTUAL_AGENTS = "powerVirtualAgents"


class DtmfTone(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DtmfTone."""

    ZERO = "zero"
    ONE = "one"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    POUND = "pound"
    ASTERISK = "asterisk"


class PlaySourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the type of the play source."""

    FILE = "file"
    TEXT = "text"
    SSML = "ssml"


class RecognitionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the sub-type of the recognize operation.
    In case of cancel operation the this field is not set and is returned empty.
    """

    DTMF = "dtmf"
    SPEECH = "speech"
    CHOICES = "choices"


class RecognizeInputType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines the type of the recognition."""

    DTMF = "dtmf"
    SPEECH = "speech"
    SPEECH_OR_DTMF = "speechOrDtmf"
    CHOICES = "choices"


class RecordingChannel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The channel type of call recording."""

    MIXED = "mixed"
    UNMIXED = "unmixed"


class RecordingContent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The content type of call recording."""

    AUDIO = "audio"
    AUDIO_VIDEO = "audioVideo"


class RecordingFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The format type of call recording."""

    WAV = "wav"
    MP3 = "mp3"
    MP4 = "mp4"


class RecordingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RecordingState."""

    ACTIVE = "active"
    INACTIVE = "inactive"


class TranscriptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TranscriptionStatus."""

    TRANSCRIPTION_STARTED = "transcriptionStarted"
    TRANSCRIPTION_FAILED = "transcriptionFailed"
    TRANSCRIPTION_RESUMED = "transcriptionResumed"
    TRANSCRIPTION_UPDATED = "transcriptionUpdated"
    TRANSCRIPTION_STOPPED = "transcriptionStopped"
    UNSPECIFIED_ERROR = "unspecifiedError"


class TranscriptionStatusDetails(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TranscriptionStatusDetails."""

    SUBSCRIPTION_STARTED = "subscriptionStarted"
    STREAM_CONNECTION_REESTABLISHED = "streamConnectionReestablished"
    STREAM_CONNECTION_UNSUCCESSFUL = "streamConnectionUnsuccessful"
    STREAM_URL_MISSING = "streamUrlMissing"
    SERVICE_SHUTDOWN = "serviceShutdown"
    STREAM_CONNECTION_INTERRUPTED = "streamConnectionInterrupted"
    SPEECH_SERVICES_CONNECTION_ERROR = "speechServicesConnectionError"
    SUBSCRIPTION_STOPPED = "subscriptionStopped"
    UNSPECIFIED_ERROR = "unspecifiedError"
    AUTHENTICATION_FAILURE = "authenticationFailure"
    BAD_REQUEST = "badRequest"
    TOO_MANY_REQUESTS = "tooManyRequests"
    FORBIDDEN = "forbidden"
    SERVICE_TIMEOUT = "serviceTimeout"
    TRANSCRIPTION_LOCALE_UPDATED = "transcriptionLocaleUpdated"


class TranscriptionTransportType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of transport to be used for live transcription, eg. Websocket."""

    WEBSOCKET = "websocket"


class VoiceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Voice kind type."""

    MALE = "male"
    FEMALE = "female"
