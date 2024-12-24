"""
# @filename    :  constants.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
from pathlib import Path

################################################################
PROJECT_ROOT_DIRECTORY = str(Path(__file__).parent.parent)
DISK_ROOT_DIRECTORY = str(Path(PROJECT_ROOT_DIRECTORY).anchor)
PYTEST_LOGS_DIRECTORY = os.path.join(DISK_ROOT_DIRECTORY, "data", "ro", "camera_test_logs")
################################################################

################################################################
DUT_CAMERA_TEST_DCIM_DIRECTORY = "/sdcard/DCIM/Camera"
DUT_CAMERA_TEST_ADB_DIRECTORY = "/sdcard/Documents/camera_test"
DUT_CAMERA_TEST_BEGIN_TIMESTAMP_FILE = os.path.join(DUT_CAMERA_TEST_ADB_DIRECTORY, "pytest3_begin_timestamp.txt")
DUT_CAMERA_TEST_END_TIMESTAMP_FILE = os.path.join(DUT_CAMERA_TEST_ADB_DIRECTORY, "pytest3_end_timestamp.txt")
DUT_CAMERA_TEST_QUIT_INDICATOR_FILE = os.path.join(DUT_CAMERA_TEST_ADB_DIRECTORY, "pytest3_quit_indicator.txt")
################################################################


def dump_constants(ulog):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.warning("DUT_CAMERA_TEST_ADB_DIRECTORY         = %s", DUT_CAMERA_TEST_ADB_DIRECTORY)
    log.warning("DUT_CAMERA_TEST_BEGIN_TIMESTAMP_FILE  = %s", DUT_CAMERA_TEST_BEGIN_TIMESTAMP_FILE)
    log.warning("DUT_CAMERA_TEST_END_TIMESTAMP_FILE    = %s", DUT_CAMERA_TEST_END_TIMESTAMP_FILE)
    log.warning("DUT_CAMERA_TEST_QUIT_INDICATOR_FILE   = %s", DUT_CAMERA_TEST_QUIT_INDICATOR_FILE)
    log.warning("DUT_CAMERA_TEST_DCIM_DIRECTORY        = %s", DUT_CAMERA_TEST_DCIM_DIRECTORY)
    return True
