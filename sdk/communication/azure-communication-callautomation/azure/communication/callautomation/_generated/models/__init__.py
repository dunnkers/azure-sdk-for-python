# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import AddParticipantFailed
from ._models import AddParticipantRequest
from ._models import AddParticipantResponse
from ._models import AddParticipantSucceeded
from ._models import AnswerCallRequest
from ._models import BaseDialog
from ._models import CallConnected
from ._models import CallConnectionProperties
from ._models import CallDisconnected
from ._models import CallIntelligenceOptions
from ._models import CallLocator
from ._models import CallParticipant
from ._models import CallTransferAccepted
from ._models import CallTransferFailed
from ._models import CancelAddParticipantFailed
from ._models import CancelAddParticipantRequest
from ._models import CancelAddParticipantResponse
from ._models import CancelAddParticipantSucceeded
from ._models import ChannelAffinity
from ._models import Choice
from ._models import ChoiceResult
from ._models import CommunicationError
from ._models import CommunicationErrorResponse
from ._models import CommunicationIdentifierModel
from ._models import CommunicationUserIdentifierModel
from ._models import ContinuousDtmfRecognitionRequest
from ._models import ContinuousDtmfRecognitionStopped
from ._models import ContinuousDtmfRecognitionToneFailed
from ._models import ContinuousDtmfRecognitionToneReceived
from ._models import CreateCallRequest
from ._models import CustomCallingContext
from ._models import DialogCompleted
from ._models import DialogConsent
from ._models import DialogFailed
from ._models import DialogHangup
from ._models import DialogLanguageChange
from ._models import DialogSensitivityUpdate
from ._models import DialogStarted
from ._models import DialogStateResponse
from ._models import DialogTransfer
from ._models import DtmfOptions
from ._models import DtmfResult
from ._models import FileSource
from ._models import HoldFailed
from ._models import HoldRequest
from ._models import MicrosoftTeamsAppIdentifierModel
from ._models import MicrosoftTeamsUserIdentifierModel
from ._models import MuteParticipantsRequest
from ._models import MuteParticipantsResult
from ._models import ParticipantsUpdated
from ._models import PhoneNumberIdentifierModel
from ._models import PlayCanceled
from ._models import PlayCompleted
from ._models import PlayFailed
from ._models import PlayOptions
from ._models import PlayRequest
from ._models import PlaySource
from ._models import PowerVirtualAgentsDialog
from ._models import RecognizeCanceled
from ._models import RecognizeCompleted
from ._models import RecognizeFailed
from ._models import RecognizeOptions
from ._models import RecognizeRequest
from ._models import RecordingStateChanged
from ._models import RecordingStateResponse
from ._models import RedirectCallRequest
from ._models import RejectCallRequest
from ._models import RemoveParticipantFailed
from ._models import RemoveParticipantRequest
from ._models import RemoveParticipantResponse
from ._models import RemoveParticipantSucceeded
from ._models import ResultInformation
from ._models import SendDtmfTonesCompleted
from ._models import SendDtmfTonesFailed
from ._models import SendDtmfTonesRequest
from ._models import SendDtmfTonesResult
from ._models import SpeechOptions
from ._models import SpeechResult
from ._models import SsmlSource
from ._models import StartCallRecordingRequest
from ._models import StartDialogRequest
from ._models import StartTranscriptionRequest
from ._models import StopTranscriptionRequest
from ._models import TeamsComplianceRecordingStateChanged
from ._models import TextSource
from ._models import TranscriptionConfiguration
from ._models import TranscriptionFailed
from ._models import TranscriptionStarted
from ._models import TranscriptionStopped
from ._models import TranscriptionUpdate
from ._models import TranscriptionUpdated
from ._models import TransferCallResponse
from ._models import TransferToParticipantRequest
from ._models import UnholdRequest
from ._models import UpdateTranscriptionRequest
from ._models import UserConsent

from ._enums import CallConnectionState
from ._enums import CallLocatorKind
from ._enums import CallRejectReason
from ._enums import CommunicationCloudEnvironmentModel
from ._enums import CommunicationIdentifierModelKind
from ._enums import DialogInputType
from ._enums import DtmfTone
from ._enums import PlaySourceType
from ._enums import RecognitionType
from ._enums import RecognizeInputType
from ._enums import RecordingChannel
from ._enums import RecordingContent
from ._enums import RecordingFormat
from ._enums import RecordingState
from ._enums import TranscriptionStatus
from ._enums import TranscriptionStatusDetails
from ._enums import TranscriptionTransportType
from ._enums import VoiceKind
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddParticipantFailed",
    "AddParticipantRequest",
    "AddParticipantResponse",
    "AddParticipantSucceeded",
    "AnswerCallRequest",
    "BaseDialog",
    "CallConnected",
    "CallConnectionProperties",
    "CallDisconnected",
    "CallIntelligenceOptions",
    "CallLocator",
    "CallParticipant",
    "CallTransferAccepted",
    "CallTransferFailed",
    "CancelAddParticipantFailed",
    "CancelAddParticipantRequest",
    "CancelAddParticipantResponse",
    "CancelAddParticipantSucceeded",
    "ChannelAffinity",
    "Choice",
    "ChoiceResult",
    "CommunicationError",
    "CommunicationErrorResponse",
    "CommunicationIdentifierModel",
    "CommunicationUserIdentifierModel",
    "ContinuousDtmfRecognitionRequest",
    "ContinuousDtmfRecognitionStopped",
    "ContinuousDtmfRecognitionToneFailed",
    "ContinuousDtmfRecognitionToneReceived",
    "CreateCallRequest",
    "CustomCallingContext",
    "DialogCompleted",
    "DialogConsent",
    "DialogFailed",
    "DialogHangup",
    "DialogLanguageChange",
    "DialogSensitivityUpdate",
    "DialogStarted",
    "DialogStateResponse",
    "DialogTransfer",
    "DtmfOptions",
    "DtmfResult",
    "FileSource",
    "HoldFailed",
    "HoldRequest",
    "MicrosoftTeamsAppIdentifierModel",
    "MicrosoftTeamsUserIdentifierModel",
    "MuteParticipantsRequest",
    "MuteParticipantsResult",
    "ParticipantsUpdated",
    "PhoneNumberIdentifierModel",
    "PlayCanceled",
    "PlayCompleted",
    "PlayFailed",
    "PlayOptions",
    "PlayRequest",
    "PlaySource",
    "PowerVirtualAgentsDialog",
    "RecognizeCanceled",
    "RecognizeCompleted",
    "RecognizeFailed",
    "RecognizeOptions",
    "RecognizeRequest",
    "RecordingStateChanged",
    "RecordingStateResponse",
    "RedirectCallRequest",
    "RejectCallRequest",
    "RemoveParticipantFailed",
    "RemoveParticipantRequest",
    "RemoveParticipantResponse",
    "RemoveParticipantSucceeded",
    "ResultInformation",
    "SendDtmfTonesCompleted",
    "SendDtmfTonesFailed",
    "SendDtmfTonesRequest",
    "SendDtmfTonesResult",
    "SpeechOptions",
    "SpeechResult",
    "SsmlSource",
    "StartCallRecordingRequest",
    "StartDialogRequest",
    "StartTranscriptionRequest",
    "StopTranscriptionRequest",
    "TeamsComplianceRecordingStateChanged",
    "TextSource",
    "TranscriptionConfiguration",
    "TranscriptionFailed",
    "TranscriptionStarted",
    "TranscriptionStopped",
    "TranscriptionUpdate",
    "TranscriptionUpdated",
    "TransferCallResponse",
    "TransferToParticipantRequest",
    "UnholdRequest",
    "UpdateTranscriptionRequest",
    "UserConsent",
    "CallConnectionState",
    "CallLocatorKind",
    "CallRejectReason",
    "CommunicationCloudEnvironmentModel",
    "CommunicationIdentifierModelKind",
    "DialogInputType",
    "DtmfTone",
    "PlaySourceType",
    "RecognitionType",
    "RecognizeInputType",
    "RecordingChannel",
    "RecordingContent",
    "RecordingFormat",
    "RecordingState",
    "TranscriptionStatus",
    "TranscriptionStatusDetails",
    "TranscriptionTransportType",
    "VoiceKind",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
