"""
# @filename    :  media.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
from typing import Union
from pymediainfo import MediaInfo
from .ulog import Ulog


def is_jpeg(ulog: Union[Ulog, None] = None, filename: str = "") -> bool:
    """
    Function : assert_eq(expected, actual)
    """
    # sanity check
    assert ulog is not None
    assert filename is not None
    assert filename != ""
    assert os.path.exists(filename)
    media_info = MediaInfo.parse(filename)
    assert len(media_info.general_tracks) > 0
    general_track = media_info.general_tracks[0]
    assert general_track.format == "JPEG", f"{filename}:expected=JPEG, actual={general_track.format}"
    return True


def is_heif(ulog: Union[Ulog, None] = None, filename: str = "") -> bool:
    """
    Function : assert_eq(expected, actual)
    """
    # sanity check
    assert ulog is not None
    assert filename is not None
    assert filename != ""
    assert os.path.exists(filename)
    media_info = MediaInfo.parse(filename)
    assert len(media_info.general_tracks) > 0
    general_track = media_info.general_tracks[0]
    assert general_track.format == "HEVC", f"{filename}:expected=HEVC, actual={general_track.format}"
    return True


def is_mp4(ulog: Union[Ulog, None] = None, filename: str = "") -> bool:
    """
    Function : assert_eq(expected, actual)
    """
    # sanity check
    assert ulog is not None
    assert filename is not None
    assert filename != ""
    assert os.path.exists(filename)
    media_info = MediaInfo.parse(filename)
    assert len(media_info.general_tracks) > 0
    general_track = media_info.general_tracks[0]
    assert general_track.format == "MPEG-4", f"{filename}:expected=MPEG-4, actual={general_track.format}"
    return True


MIMES_VERIFIER = {"jpg": is_jpeg, "mp4": is_mp4, "heif": is_heif}


def verify(ulog: Union[Ulog, None] = None, filename: str = "", mime: str = "") -> bool:
    """
    Function : assert_eq(expected, actual)
    """
    # sanity check
    assert ulog is not None
    assert mime is not None
    assert mime in MIMES_VERIFIER
    assert MIMES_VERIFIER[mime](filename)
    return True
