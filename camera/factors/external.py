"""
# @filename    :  external.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-08T16:09:59+08:00
"""

from typing import Union
import random
import time
from utils.ulog import Ulog

ANDROID_PACKAGES = (
    "com.android.settings",
    "com.android.chrome",
    "com.google.android.youtube",
    "com.google.android.calendar",
    "com.google.android.deskclock",
    "com.google.android.dialer",
    "com.google.android.contacts",
    "com.google.android.calculator",
    "com.google.android.apps.wellbeing",
    "com.google.android.apps.googleassistant",
    "com.google.android.apps.tachyon",
    "com.google.android.apps.youtube.music",
    "com.google.android.apps.maps",
    "com.google.android.apps.docs",
    "com.google.android.apps.safetyhub",
    "com.google.android.apps.messaging",
    "com.google.android.apps.photos",
)
# ANDROID_PACKAGES = ("com.android.chrome", "com.google.android.apps.photos")
HMDGLOBAL_PACKAGES = ("com.hmdglobal.support", "com.hmdglobal.app.consumertrials")

# RAMSIZE:CACHED_PACKAGE_NUMBER
RAM_CACHE_DICT = {"4GB": 3, "6GB": 5, "8GB": 7, "12GB": 11}


def do_apps_start_stop(ulog: Union[Ulog, None] = None):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()

    ramsize = ulog.get_udev().get_ramsize()
    assert ramsize in RAM_CACHE_DICT
    # cached_package_number = RAM_CACHE_DICT[ramsize]
    cached_package_number = 3
    for each in random.sample(ANDROID_PACKAGES + HMDGLOBAL_PACKAGES, cached_package_number):
        log.info("start:%s", each)
        device.app_start(each)
        time.sleep(3)
        device.app_stop(each)
        log.info("stop:%s", each)
        time.sleep(3)


def do_apps_start(ulog: Union[Ulog, None] = None):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()

    ramsize = ulog.get_udev().get_ramsize()
    assert ramsize in RAM_CACHE_DICT
    # cached_package_number = RAM_CACHE_DICT[ramsize]
    cached_package_number = 3
    for each in random.sample(ANDROID_PACKAGES + HMDGLOBAL_PACKAGES, cached_package_number):
        device.app_start(each)
        log.info("start:%s", each)
        time.sleep(2)


def do_apps_stop(ulog: Union[Ulog, None] = None):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()

    ramsize = ulog.get_udev().get_ramsize()
    assert ramsize in RAM_CACHE_DICT
    # cached_package_number = RAM_CACHE_DICT[ramsize]
    cached_package_number = 3
    for each in random.sample(ANDROID_PACKAGES + HMDGLOBAL_PACKAGES, cached_package_number):
        device.app_stop(each)
        log.info("start:%s", each)
        time.sleep(2)


# EXTERNAL_FACTORS = (do_apps)
