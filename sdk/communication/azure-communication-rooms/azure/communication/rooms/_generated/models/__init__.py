# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.3, generator: @autorest/python@6.4.7)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import CommunicationError
from ._models import CommunicationErrorResponse
from ._models import CommunicationRoom
from ._models import CreateRoomRequest
from ._models import ParticipantProperties
from ._models import RoomParticipant
from ._models import UpdateParticipantsRequest
from ._models import UpdateRoomRequest

from ._enums import ParticipantRole
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CommunicationError",
    "CommunicationErrorResponse",
    "CommunicationRoom",
    "CreateRoomRequest",
    "ParticipantProperties",
    "RoomParticipant",
    "UpdateParticipantsRequest",
    "UpdateRoomRequest",
    "ParticipantRole",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()