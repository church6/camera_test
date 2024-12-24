"""
# @filename    :  enums.py
# @author      :  Copyright (C) Church.ZHONG
"""

from enum import Enum


class EnumTombstone(Enum):
    """
    Class : python 3.4 support Enum
    """

    TYPE_NONE = 0
    TYPE_CAMERA_PROVIDER = 1
    TYPE_CAMERA_SERVER = 2


class EnumException(Enum):
    """
    Class : python 3.4 support Enum
    """

    TYPE_NONE = 0
    TYPE_CAMERA_APP_CRASH = 1
    TYPE_CAMERA_APP_ERROR = 2
    TYPE_ANR = 3
    TYPE_POPUP = 4


class EnumDeviceChargeState(Enum):
    """
    Class : python 3.4 support Enum
    """

    TYPE_NONE = 0
    TYPE_DEVICE_IS_NOT_IN_CHARGING = 1
    TYPE_DEVICE_IS_YES_IN_CHARGING = 2
