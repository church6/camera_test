"""
# @author      :  Copyright (C) Church.ZHONG
"""

__version__ = "0.0.1"
__author__ = "Church.ZHONG"
__all__ = ["catch_error"]

from typing import Union
from datetime import datetime
from utils.enums import EnumException
from .detector import ExceptionDetector


def catch_error(timestamp: Union[str, None] = None, ulog=None, witness: Union[str, None] = None, forced: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert witness is not None
    # [enter]What time did the exception occur?
    if timestamp is None or timestamp == "":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # [leave]What time did the exception occur?
    error = False
    with ExceptionDetector(ulog=ulog, timestamp=timestamp, witness=witness, forced=forced) as detector:
        if detector.get_exception_type() in [
            EnumException.TYPE_CAMERA_APP_CRASH,
            EnumException.TYPE_CAMERA_APP_ERROR,
            EnumException.TYPE_ANR,
        ]:
            error = True
    return error
