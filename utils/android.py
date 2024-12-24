# pylint: disable=C0301
"""
# @filename    :  android.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
import time
from typing import Union
from retry import retry
from .features import get_variant_feature_by_product, get_node_by_key
from .constants import (
    DUT_CAMERA_TEST_ADB_DIRECTORY,
    DUT_CAMERA_TEST_DCIM_DIRECTORY,
    DUT_CAMERA_TEST_BEGIN_TIMESTAMP_FILE,
    DUT_CAMERA_TEST_END_TIMESTAMP_FILE,
    dump_constants,
)
from .run import run
from .views import information, found, click
from .ulog import Ulog
from .enums import EnumDeviceChargeState


################################################################
# adb methods without Ulog
################################################################
def adb(serial_number: Union[str, None] = None, command: Union[str, None] = None, block: bool = True):
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    assert command is not None
    get = run(rf"adb -s {serial_number} {command}", block=block)
    # print(f"{command} = {get.status}")
    return get


def adb_clean_dir(serial_number: Union[str, None] = None, directory: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    assert directory is not None
    adb(serial_number, f"shell mkdir -p {directory}")
    adb(serial_number, f"shell find {directory} -type dfs | xargs rm -fr")
    return True


def adb_volume_down(serial_number: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    for dummy in range(10):
        assert adb(serial_number, "shell input keyevent KEYCODE_VOLUME_DOWN").status
        time.sleep(0.5)
    return True


def root_device(serial_number: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    print(f"[enter]root_device:{serial_number}")
    assert adb_volume_down(serial_number)
    assert adb(serial_number, "shell locksettings set-disabled true").status
    assert adb(serial_number, "shell settings put system screen_off_timeout 2147483647").status
    assert adb(serial_number, "shell settings put global heads_up_notifications_enabled 0").status
    assert adb(serial_number, "shell settings put system accelerometer_rotation 0").status
    assert adb(serial_number, "shell settings put system user_rotation 0").status
    assert adb(serial_number, "shell wm user-rotation lock 0").status
    assert adb(serial_number, "shell cmd location set-location-enabled true").status
    assert adb(serial_number, "shell cmd notification set_dnd on").status
    assert adb(serial_number, "shell cmd bluetooth_manager disable").status
    assert adb(serial_number, "shell cmd wifi set-wifi-enabled enabled").status
    assert adb(serial_number, "shell cmd connectivity airplane-mode disable").status
    # [enter][Turn off Battery Optimization]
    assert adb(serial_number, "shell dumpsys deviceidle whitelist +com.github.uiautomator").status
    assert adb(serial_number, "shell dumpsys deviceidle whitelist +com.github.uiautomator.test").status
    # [leave][Turn off Battery Optimization]
    assert adb(serial_number, "shell settings put global development_settings_enabled 1").status
    assert adb(serial_number, "root").status

    # [enter][time and language]
    assert adb(serial_number, "shell settings put system init_language_value en-GB").status
    assert adb(serial_number, "shell settings put system system_locales en-GB").status
    assert adb(serial_number, "shell settings put system time_12_24 24").status
    assert adb(serial_number, 'shell settings put global time_zone "China/Shanghai"').status
    assert adb(serial_number, "shell settings put global auto_time 1").status
    # [leave][time and language]
    # [enter][timezone]
    assert adb(serial_number, "shell cmd time_zone_detector set_auto_detection_enabled fasle").status
    assert adb(serial_number, "shell cmd time_zone_detector set_geo_detection_enabled false").status
    assert adb(serial_number, "shell settings put secure location_time_zone_detection_enabled 0").status
    assert adb(serial_number, "shell settings put secure location_background_throttle_interval_ms 6000000").status
    assert adb(serial_number, "shell cmd location_time_zone_manager stop").status
    # [leave][timezone]
    assert adb(serial_number, "shell settings put global isfirst_battery_protection 0").status
    assert adb(serial_number, "shell settings put global battery_charging_state_enforce_level 80").status
    assert adb(serial_number, "shell settings put global battery_protection_status 0").status
    assert adb(serial_number, "shell settings put global limit_maximum_battery 1").status

    # [enter][clean]
    adb_clean_dir(serial_number, DUT_CAMERA_TEST_ADB_DIRECTORY)
    adb_clean_dir(serial_number, DUT_CAMERA_TEST_DCIM_DIRECTORY)
    adb_clean_dir(serial_number, "/data/vendor/camera/coredump")
    adb_clean_dir(serial_number, "/data/anr")
    # [enter][reboot to take effect]
    #### adb_clean_dir(serial_number, "/data/tombstones")
    # [leave][reboot to take effect]
    adb_clean_dir(serial_number, "/data/system/dropbox")
    # [leave][clean]
    print(f"[leave]root_device:{serial_number}")
    return True


################################################################
# adb methods within Ulog
################################################################
def device_enable_camera(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("enter")
    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME
    assert ulog.adb(f"shell pm enable {camera_package_name}").status
    log.info("leave")
    return True


def watcher_setup(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    log.info("add and start watchers")
    # device.watcher.when("Got it").press("Got it")
    # device.watcher.when("Feedback").press("CANCEL")
    # device.watcher.when("keeps stopping").press("Close app")
    device.watcher.start()
    return True


def watcher_teardown(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    status = True
    device.watcher.stop()
    device.watcher.remove()
    log.info("stop and remove all watchers")
    return status


def device_dim_screen(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("enter")
    # [enter][enable camera brightness enhancement]
    assert ulog.adb("shell settings put system screen_brightness_mode 1").status
    # [leave][enable camera brightness enhancement]
    assert ulog.adb("shell settings put system screen_brightness 50").status
    log.info("leave")
    return True


def device_dark_theme(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    android_settings_package_name = get_variant_feature_by_product(ulog=ulog).ANDROID_SETTINGS_PACKAGE_NAME
    device.app_stop(package_name=android_settings_package_name)
    assert ulog.adb("shell input keyevent --longpress KEYCODE_HOME").status
    time.sleep(0.2)
    assert ulog.adb("shell am start -a android.settings.DISPLAY_SETTINGS").status
    time.sleep(0.2)
    key = "dark theme toggle"
    node = get_node_by_key(ulog=ulog, key=key)
    assert device(scrollable=True).scroll.to(**node), key
    info = information(ulog=ulog, key=key)
    assert info is not None, key
    assert "checked" in info, key
    if info["checked"]:
        log.warning("was dark")
    else:
        log.warning("%s:click", key)
        assert click(ulog=ulog, key=key)
        time.sleep(0.2)
    device.app_stop(package_name=android_settings_package_name)
    return True


@retry(tries=3, delay=0.5, logger=None)
def device_go_home(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    device = ulog.get_device()
    device.screen_on()
    if found(ulog=ulog, key="home screen"):
        return True
    if found(ulog=ulog, key="wakeup screen"):
        device.unlock()
        device.swipe_ext(direction="up", scale=0.8)
    return True


def device_setup(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    assert ulog.adb(rf'shell "echo \${{EPOCHREALTIME}} >{DUT_CAMERA_TEST_BEGIN_TIMESTAMP_FILE}"').status
    device = ulog.get_device()
    # watcher_setup(ulog=ulog)
    device_go_home(ulog=ulog)
    device.set_orientation("natural")
    device.freeze_rotation()
    device.show_float_window()
    device_dim_screen(ulog=ulog)
    device_dark_theme(ulog=ulog)
    dump_constants(ulog=ulog)
    device_enable_camera(ulog=ulog)
    # [enter][Allow display over other apps]
    assert ulog.adb("shell pm grant com.github.uiautomator android.permission.SYSTEM_ALERT_WINDOW").status
    # [leave][Allow display over other apps]
    assert setup_feedback(ulog=ulog)
    log.info("setup done")
    return True


def device_teardown(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    # watcher_teardown(ulog=ulog)
    assert ulog.adb(rf'shell "echo \${{EPOCHREALTIME}} >{DUT_CAMERA_TEST_END_TIMESTAMP_FILE}"').status
    # [enter][pull]comes last
    pull_crash(ulog=ulog)
    # [leave][pull]comes last
    log.info("teardown done")
    return True


def __do_charge__(ulog: Union[Ulog, None] = None, charge_time=30) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert charge_time > 0
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    battery_capacity = ulog.get_udev().get_battery_capacity()
    ulog.set_shared_number1(EnumDeviceChargeState.TYPE_DEVICE_IS_YES_IN_CHARGING)
    log.warning("[enter]battery=%03d,charge=%ds", battery_capacity, charge_time)
    device_dim_screen(ulog=ulog)
    device.screen_off()
    time.sleep(charge_time)
    device_go_home(ulog=ulog)
    battery_capacity = ulog.get_udev().get_battery_capacity()
    log.warning("[leave]battery=%03d,charge=%ds", battery_capacity, charge_time)
    ulog.set_shared_number1(EnumDeviceChargeState.TYPE_DEVICE_IS_NOT_IN_CHARGING)
    device_dim_screen(ulog=ulog)
    return True


def device_long_charge(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    # __do_charge__(ulog=ulog, charge_time=14400)
    return True


def pull_crash(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    crash_directory = ulog.get_crash_directory()
    log.info("%s", crash_directory)
    directories = [
        DUT_CAMERA_TEST_ADB_DIRECTORY,
        "/data/vendor/camera/coredump",
        "/data/anr",
        "/data/tombstones",
        "/data/system/dropbox",
        "/data/local/hmdlogs",
    ]
    for each in directories:
        get = ulog.adb(f"pull {each} {crash_directory}")
        print(f"pull {each}={get.status}")

    dumpsys_dropbox_filename = os.path.join(DUT_CAMERA_TEST_ADB_DIRECTORY, "dumpsys_dropbox.log")
    assert ulog.adb(f'shell "dumpsys dropbox -p >{dumpsys_dropbox_filename}"').status
    assert ulog.adb(f"pull {dumpsys_dropbox_filename} {crash_directory}").status
    # [enter][clean hmdlogs]
    ulog.adb("shell \"find /data/local/hmdlogs -type f -name '*.gz' | xargs rm -f\"")
    # [leave][clean hmdlogs]
    return True


@retry(tries=3, delay=0.5, logger=None)
def setup_feedback(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog.adb("shell am start -n com.hmdglobal.app.activation/com.hmdglobal.app.activation.nps.MainDialogActivity").status
    time.sleep(1)
    key = "activation scoreseekbar"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key)
    key = "activation next button"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key)
    key = "activation donot again"
    if found(ulog=ulog, key=key):
        info = information(ulog=ulog, key=key)
        assert info is not None
        assert "checked" in info
        if not info["checked"]:
            assert click(ulog=ulog, key=key)
    key = "activation comment"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key)
        device = ulog.get_device()
        device.clear_text()
        time.sleep(0.2)
        comment = "This comment is generated by Automated Testing Tool from Church.ZHONG@hmdglobal.com.\n"
        comment += "Please ignore this comment.\n"
        device.send_keys(comment)
    key = "activation done button"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key)
    key = "activation ok button"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key)
    return True
