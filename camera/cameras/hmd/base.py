# pylint: disable=C0302
"""
# @filename    :  base.py
# @author      :  Copyright (C) Church.ZHONG
# @function    :  operate camera with less but important logging
"""

import time
from typing import Union
import functools
from retry import retry
from utils.dcim import do_validate
from utils.ulog import Ulog
from utils.views import information, found, click, long_click
from utils.features import get_variant_feature_by_product


def is_low_battery_capacity(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    battery_capacity = ulog.get_udev().get_battery_capacity()
    low_battery_capacity = battery_capacity < 16
    if low_battery_capacity:
        log.warning("battery_capacity=%d", battery_capacity)
    return low_battery_capacity


################################################################
# define file_validator decorator
################################################################
def file_validator(mime: str = "", quantity: int = 1):
    """
    Function : decorator
    """

    def file_validator_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            assert "reserved" in kwargs
            ulog, reserved = kwargs["ulog"], kwargs["reserved"]
            log = ulog.get_camera_logger()
            log.info("enter=%s", func.__name__)
            if ulog.is_dimlight():
                set_flash(ulog=ulog, mode="flash on")
            assert func(*args, **kwargs)
            log.info("leave=%s", func.__name__)
            heif_format_enabled = ulog.get_ucam().get_enabled_by_key(key="heif format toggle")
            validate_mime = "heif" if func.__name__ == "take_photo" and heif_format_enabled else mime
            validate_quantity = quantity
            assert do_validate(ulog, reserved, validate_mime, validate_quantity, func.__name__)
            return True

        return wrapper

    return file_validator_wrapper


################################################################
# define zoom_ratio_shielder decorator
################################################################
def zoom_ratio_shielder(func):
    """
    Function : decorator
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Function :
        """
        # sanity check
        assert "ulog" in kwargs
        ulog = kwargs["ulog"]
        key = "scan qrcode toggle"
        current = ulog.get_ucam().get_enabled_by_key(key=key)
        if current:
            # temporarily disable
            assert toggle_scan_qrcode(ulog=ulog, enable=False)
        value = func(*args, **kwargs)
        if current:
            # voluntarily enable
            assert toggle_scan_qrcode(ulog=ulog, enable=True)
        return value

    return wrapper


################################################################
# define actions of camera module
################################################################
def set_camera_permission(ulog: Union[Ulog, None] = None, package_name: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert package_name is not None

    key = "location permission button allow"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key), key

    key = "notifications permission button allow"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key), key

    return True


def set_camera_agenda(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    # New Camera UX/UI
    key = "agenda button"
    if not click(ulog=ulog, key=key):
        return False

    key = "next button"
    for dummy in range(9):
        if not found(ulog=ulog, key=key):
            return True
        assert click(ulog=ulog, key=key), key
    return True


class DropdownSettingsWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "more settings closed button"
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
            if found(ulog=self.ulog, key="more settings opened button"):
                break
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            key = "more settings opened button"
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
            if found(ulog=self.ulog, key="more settings closed button"):
                break

    def toggle(self, key: Union[str, None] = None, enable: bool = False) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        log = self.ulog.get_camera_logger()
        info = information(ulog=self.ulog, key=key)
        if info is not None and "enabled" in info and info["enabled"] != enable:
            log.info("[enter]%s=%s", str(enable), key)
            assert click(ulog=self.ulog, key=key), key
            log.info("[leave]%s=%s", str(enable), key)
        return True

    def touch(self, key: Union[str, None] = None) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        log = self.ulog.get_camera_logger()
        if found(ulog=self.ulog, key=key):
            log.info("[enter]key=%s", key)
            assert click(ulog=self.ulog, key=key), key
            log.info("[leave]key=%s", key)
        return True


def toggle_dropdown_settings_by_key(ulog: Union[Ulog, None] = None, key: Union[str, None] = None, enable: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    with DropdownSettingsWorker(ulog=ulog) as worker:
        assert worker.toggle(key, enable)
    return True


def set_dropdown_settings_by_key(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    with DropdownSettingsWorker(ulog=ulog) as worker:
        assert worker.touch(key)
    return True


def change_dropdown_settings(ulog: Union[Ulog, None] = None, enable: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()

    log.info("enter")
    for each in [
        # "watermark toggle",
        "high resolution toggle",
        "focus peaking toggle",
        # "eyes tracking toggle", # default is enabled
        "selfie gesture toggle",
        "grid toggle",
        "level meter toggle",
    ]:
        assert toggle_dropdown_settings_by_key(ulog=ulog, key=each, enable=enable)
    log.info("leave")

    return True


class GlobalSettingsWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "more settings closed button"
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
            if found(ulog=self.ulog, key="more settings opened button"):
                break
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "settings imageview"
            if found(ulog=self.ulog, key=key) and click(ulog=self.ulog, key=key):
                if found(ulog=self.ulog, key="navigate up"):
                    break
            key = "settings lefttop"
            if found(ulog=self.ulog, key=key) and click(ulog=self.ulog, key=key):
                if found(ulog=self.ulog, key="navigate up"):
                    break
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key="navigate up"):
                assert click(ulog=self.ulog, key="navigate up")
            if found(ulog=self.ulog, key="more settings closed button"):
                break

    def toggle(self, key: Union[str, None] = None) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        log = self.ulog.get_camera_logger()
        if key == "ozo audio toggle":
            device = self.ulog.get_device()
            device.swipe_ext(direction="up", scale=0.8)
        log.info("click:%s", key)
        assert click(ulog=self.ulog, key=key), key
        if key == "long press on shutter":
            assert click(ulog=self.ulog, key="burst shots radio button")
        self.ulog.get_ucam().toggle_enabled_by_key(key=key)
        log.info("%s=%s", self.ulog.get_ucam().get_enabled_by_key(key=key), key)
        return True


def toggle_global_settings_by_key(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    with GlobalSettingsWorker(ulog=ulog) as worker:
        assert worker.toggle(key)
    return True


def change_global_settings(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("enter")
    # [enter][global settings]
    with GlobalSettingsWorker(ulog=ulog) as worker:
        for each in ulog.get_ucam().get_global_settings_keys():
            assert worker.toggle(key=each)
    # [leave][global settings]
    log.info("leave")
    return True


def toggle_scan_qrcode(ulog: Union[Ulog, None] = None, enable: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "scan qrcode toggle"
    if ulog.get_ucam().get_enabled_by_key(key=key) != enable:
        assert toggle_global_settings_by_key(ulog=ulog, key=key)
        assert ulog.get_ucam().get_enabled_by_key(key=key) is enable
    return True


def open_camera(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    assert device is not None
    log.info("enter")
    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME

    # start package by name
    device.screen_on()
    device.app_start(package_name=camera_package_name, wait=True, stop=True)
    # [enter]unstable uiautomator2
    time.sleep(1.5)
    # [leave]unstable uiautomator2

    # [enter]cleared
    current_package_name = device.app_current()["package"]
    if current_package_name == get_variant_feature_by_product(ulog=ulog).GOOGLE_PERMISSION_CONTROLLER_PACKAGE_NAME:
        log.warning("package:%s", current_package_name)
        assert set_camera_permission(ulog, current_package_name)
        # [enter]unstable uiautomator2
        time.sleep(1.5)
        # [leave]unstable uiautomator2
    current_package_name = device.app_current()["package"]
    key = "agenda button"
    if current_package_name == camera_package_name and found(ulog=ulog, key=key):
        log.warning("package:%s", current_package_name)
        assert set_camera_agenda(ulog)
        # [enter]unstable uiautomator2
        time.sleep(1.5)
        # [leave]unstable uiautomator2
        ulog.get_ucam().reset_global_settings()

        # [enter]disable AI portrait for "back camera"
        set_reverse(ulog=ulog, camera="back camera")
        set_aiportrait(ulog=ulog, mode="ai portrait on")
        # [leave]disable AI portrait for "back camera"
        assert change_dropdown_settings(ulog=ulog, enable=False)

        # [enter]disable AI portrait for "front camera"
        set_reverse(ulog=ulog, camera="front camera")
        set_aiportrait(ulog=ulog, mode="ai portrait on")
        # [leave]disable AI portrait for "front camera"
        assert change_dropdown_settings(ulog=ulog, enable=False)
        assert change_global_settings(ulog)
    # [leave]cleared

    assert set_reverse(ulog, camera="back camera")
    log.info("leave")
    return True


def close_camera(ulog: Union[Ulog, None] = None, clear: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    device = ulog.get_device()
    assert device is not None
    log.info("enter")
    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME

    # stop package by name
    device.app_stop(package_name=camera_package_name)
    if clear:
        # [enter]unstable uiautomator2
        time.sleep(1.5)
        # [leave]unstable uiautomator2
        device.app_clear(package_name=camera_package_name)
        ulog.get_ucam().reset_global_settings()
        log.warning("clear camera")

    log.info("leave")
    return True


def restart_camera(ulog: Union[Ulog, None] = None, clear=False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert close_camera(ulog=ulog, clear=clear)
    assert open_camera(ulog=ulog)
    return True


def warmup_camera(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    device = ulog.get_device()
    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME

    # start package by name
    device.app_start(package_name=camera_package_name, wait=True, stop=True)
    # [enter]unstable uiautomator2
    time.sleep(1)
    # [leave]unstable uiautomator2
    # stop package by name
    device.app_stop(package_name=camera_package_name)

    # [enter]unstable uiautomator2
    time.sleep(1)
    # [leave]unstable uiautomator2
    device.app_clear(package_name=camera_package_name)

    assert open_camera(ulog=ulog)
    assert close_camera(ulog=ulog, clear=False)
    return True


def check_zoom(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    info = information(ulog=ulog, key=key)
    assert info is not None, key
    assert "selected" in info, key
    assert info["selected"], key
    log.info("key=%s", key)
    return True


@zoom_ratio_shielder
def get_zoom(ulog: Union[Ulog, None] = None) -> str:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    mode = "default"
    for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"]:
        info = information(ulog=ulog, key=each)
        if info is not None and "selected" in info and info["selected"]:
            mode = each
            break
    log.info("mode=%s", mode)
    return mode


@zoom_ratio_shielder
def set_zoom(ulog: Union[Ulog, None] = None, mode: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert mode is not None
    assert mode in ["default", "zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"]
    if mode == "default":
        return True

    key = mode
    for dummy in range(3):
        if found(ulog=ulog, key=key) and click(ulog=ulog, key=key):
            # click three times
            # [enter][tuned]wait to preview
            time.sleep(0.2)
            # [leave][tuned]wait to preview

    # [enter][assert][validate]
    assert check_zoom(ulog=ulog, key=key)
    # [leave][assert][validate]
    return True


def check_hdr(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    assert found(ulog=ulog, key=key), key
    log.info("key=%s", key)
    return True


def get_hdr(ulog: Union[Ulog, None] = None) -> str:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    mode = "default"
    for each in ["hdr auto", "hdr on", "hdr off"]:
        key = f"{each} toggle"
        if found(ulog=ulog, key=key):
            mode = each
            break
    log.info("mode=%s", mode)
    return mode


def set_hdr(ulog: Union[Ulog, None] = None, mode: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert mode is not None
    assert mode in ["default", "hdr auto", "hdr on", "hdr off"]
    if mode == "default":
        return True

    current = get_hdr(ulog=ulog)
    if current == "default":
        return True
    if current == mode:
        return True

    key = f"{current} toggle"
    if not click(ulog=ulog, key=key):
        return False

    key = mode
    assert click(ulog=ulog, key=key), key

    # [enter][assert][validate]
    key = f"{mode} toggle"
    assert check_hdr(ulog=ulog, key=key)
    # [leave][assert][validate]
    return True


def check_reverse(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function : alias of check_camera
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    assert found(ulog=ulog, key=key), key
    log.info("key=%s", key)
    return True


def get_reverse(ulog: Union[Ulog, None] = None) -> str:
    """
    Function : alias of get_camera
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()

    camera = "default camera"
    for each in ["back camera", "front camera"]:
        if found(ulog=ulog, key=each):
            camera = each
            break
    log.info("camera=%s", camera)

    return camera


def set_reverse(ulog: Union[Ulog, None] = None, camera: Union[str, None] = None) -> bool:
    """
    Function : alias of set_camera
    """
    # sanity check
    assert ulog is not None
    assert camera is not None
    assert camera in ["default camera", "back camera", "front camera"]
    if camera == "default camera":
        return True

    current = get_reverse(ulog=ulog)
    if current == "default camera":
        return True
    if current == camera:
        return True

    # toggle button
    assert click(ulog=ulog, key=current), current

    # [enter][assert][validate]
    assert check_reverse(ulog=ulog, key=camera)
    # [leave][assert][validate]
    return True


def check_flash(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    assert found(ulog=ulog, key=key), key
    log.info("key=%s", key)
    return True


def get_flash(ulog: Union[Ulog, None] = None) -> str:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    mode = "default"
    for each in ["flash auto", "flash on", "flash off", "torch on"]:
        key = f"{each} toggle"
        if found(ulog=ulog, key=key):
            mode = each
            break
    log.info("mode=%s", mode)
    return mode


def set_flash(ulog: Union[Ulog, None] = None, mode: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # pylint: disable=R0911
    # sanity check
    assert ulog is not None
    assert mode is not None
    assert mode in ["default", "flash auto", "flash on", "flash off", "torch on"]
    if mode == "default":
        return True

    # [enter]Low battery, Flash disabled.
    if is_low_battery_capacity(ulog):
        return True
    # [leave]Low battery, Flash disabled.

    current = get_flash(ulog=ulog)
    if current == "default":
        return True
    if current == mode:
        return True

    key = f"{current} toggle"
    assert click(ulog=ulog, key=key), key

    key = mode
    if not found(ulog=ulog, key=key):
        # do NOT support
        return True
    assert click(ulog=ulog, key=key), key

    # [enter][assert][validate]
    key = f"{mode} toggle"
    assert check_flash(ulog=ulog, key=key)
    # [leave][assert][validate]
    return True


def check_aiportrait(ulog: Union[Ulog, None] = None, key: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    assert found(ulog=ulog, key=key), key
    log.info("key=%s", key)
    return True


def get_aiportrait(ulog: Union[Ulog, None] = None) -> str:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    mode = "default"
    for each in ["ai portrait on", "ai portrait off"]:
        if found(ulog=ulog, key=each):
            mode = each
            break
    log.info("mode=%s", mode)
    return mode


def set_aiportrait(ulog: Union[Ulog, None] = None, mode: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert mode is not None
    assert mode in ["default", "ai portrait on", "ai portrait off"]
    if mode == "default":
        return True

    current = get_aiportrait(ulog=ulog)
    if current == "default":
        return True
    if mode == current:
        return True

    assert click(ulog=ulog, key=current), current

    # [enter][assert][validate]
    assert check_aiportrait(ulog=ulog, key=mode)
    # [leave][assert][validate]
    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview
    return True


def get_beauty(ulog: Union[Ulog, None] = None) -> str:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    mode = "default"
    # [enter][photo]
    if found(ulog=ulog, key="skintone mode"):
        info = information(ulog=ulog, key="skintone natural mode")
        assert info is not None
        assert "selected" in info
        if info["selected"]:
            mode = "skintone natural mode"
        else:
            mode = "skintone bright mode"
    elif found(ulog=ulog, key="beauty mode"):
        mode = "beauty mode"
    # [leave][photo]
    # [enter][portrait]
    elif found(ulog=ulog, key="bokeh mode"):
        mode = "bokeh mode"
    elif found(ulog=ulog, key="beautify mode"):
        mode = "beautify mode"
    # [leave][portrait]
    log.info("mode=%s", mode)
    return mode


def set_beauty(ulog: Union[Ulog, None] = None, mode: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert mode is not None
    assert mode in ["default", "beauty mode", "skintone natural mode", "skintone bright mode", "bokeh mode", "beautify mode"]
    log = ulog.get_camera_logger()

    if mode == "default":
        return True

    current = get_beauty(ulog=ulog)
    if mode == current:
        return True

    key = "beauty menu button"
    if found(ulog=ulog, key=key):
        assert click(ulog=ulog, key=key), key
    else:
        return True

    if mode in ["skintone natural mode", "skintone bright mode"]:
        if not found(ulog=ulog, key="skintone mode"):
            return True
        assert click(ulog=ulog, key="skintone mode"), "skintone mode"

    if not found(ulog=ulog, key=mode):
        return True
    assert click(ulog=ulog, key=mode), mode
    log.info("mode=%s", current)

    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview

    return True


def set_pinchout(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    assert click_center(ulog=ulog)
    device = ulog.get_device()
    percent_m, steps_m = 45, 15
    for dummy in range(16):
        device().pinch_out(percent=percent_m, steps=steps_m)
    return True


def set_pinchin(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    assert click_center(ulog=ulog)
    device = ulog.get_device()
    percent_m, steps_m = 45, 15
    for dummy in range(16):
        device().pinch_in(percent=percent_m, steps=steps_m)
    return True


def click_more(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "more functions"
    assert setup_photo(ulog=ulog), key
    for dummy in range(3):
        if found(ulog=ulog, key=key):
            assert click(ulog=ulog, key=key), key
            break
    assert found(ulog=ulog, key="edit button")
    return True


def click_center(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    (width, height) = ulog.get_display()
    device = ulog.get_device()
    device.click(width // 2, height // 2)

    return True


def click_shutter(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "shutter"
    if not click(ulog=ulog, key=key, noop=0):
        return False

    return True


def setup_video(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "video"
    if not found(ulog=ulog, key=key):
        assert setup_photo(ulog=ulog), key
    if not click(ulog=ulog, key=key):
        return False
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_video(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function : time.sleep(1) is NOT accurate or expected for multiprocessing
    Function : time.sleep(1) is TOO short to record video
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    log = ulog.get_camera_logger()

    log.info("enter=%.2f", duration)
    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="video") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2
    log.info("leave=%.2f", duration)

    # [enter]unstable uiautomator2
    noop = 2 if 0 < duration <= 16 else 4
    time.sleep(noop)
    # [leave]unstable uiautomator2

    return True


def teardown_video(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    return True


@retry(tries=3, delay=0.2, logger=None)
def setup_photo(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "photo"
    assert click(ulog=ulog, key=key), key
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_photo(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview

    assert click_shutter(ulog=ulog)

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_photo(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    return True


def setup_portrait(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "portrait"
    if not found(ulog=ulog, key=key):
        assert setup_photo(ulog=ulog), key
    if not click(ulog=ulog, key=key):
        return False
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_portrait(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview

    assert click_shutter(ulog=ulog)

    # [enter][tuned]unstable uiautomator2
    time.sleep(9)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_portrait(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    return True


def setup_night(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "night"
    if not found(ulog=ulog, key=key):
        assert setup_photo(ulog=ulog), key
    if not click(ulog=ulog, key=key):
        return False
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_night(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview

    assert click_shutter(ulog=ulog)

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_night(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    return True


def setup_burstshot(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert setup_photo(ulog=ulog), "burstshot"
    return True


@file_validator(mime="jpg", quantity=2)
def take_burstshot(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    # [enter][tuned]wait to preview
    time.sleep(0.5)
    # [leave][tuned]wait to preview

    assert long_click(ulog=ulog, key="shutter", duration=duration)
    # [enter][tuned]unstable uiautomator2
    time.sleep(2)
    # [leave][tuned]unstable uiautomator2
    assert found(ulog=ulog, key="photo")

    # [enter][tuned]unstable uiautomator2
    time.sleep(6)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_burstshot(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    return True


def setup_flashshot(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave flashshot"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter flashshot"), "enter flashshot"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=5)
def take_flashshot(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    # [enter][tuned]unstable uiautomator2
    time.sleep(6)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_flashshot(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave flashshot"
    assert click(ulog=ulog, key=key), key
    return True


def setup_dualsight(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave dualsight"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter dualsight"), "enter dualsight"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_dualsight(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="leave dualsight") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_dualsight(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave dualsight"
    assert click(ulog=ulog, key=key), key
    return True


def setup_timelapse(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave timelapse"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter timelapse"), "enter timelapse"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_timelapse(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="leave timelapse") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_timelapse(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave timelapse"
    assert click(ulog=ulog, key=key), key
    return True


def setup_panorama(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave panorama"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter panorama"), "enter panorama"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_panorama(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(1)
    assert click_shutter(ulog=ulog)

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_panorama(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave panorama"
    assert click(ulog=ulog, key=key), key
    return True


def setup_slowmotion(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave slowmotion"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter slowmotion"), "enter slowmotion"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_slowmotion(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="leave slowmotion") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_slowmotion(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave slowmotion"
    assert click(ulog=ulog, key=key), key
    return True


def setup_professional(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave professional"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter professional"), "enter professional"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_professional(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_professional(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave professional"
    assert click(ulog=ulog, key=key), key
    return True


def setup_speedwarp(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave speedwarp"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter speedwarp"), "enter speedwarp"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_speedwarp(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="leave speedwarp") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_speedwarp(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave speedwarp"
    assert click(ulog=ulog, key=key), key
    return True


def setup_astrophoto(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave astrophoto"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter astrophoto"), "enter astrophoto"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="jpg", quantity=1)
def take_astrophoto(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    # [enter][tuned]unstable uiautomator2
    time.sleep(6)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_astrophoto(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave astrophoto"
    assert click(ulog=ulog, key=key), key
    return True


def setup_ultrasteadyvideo(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None

    key = "leave ultrasteadyvideo"
    if not found(ulog=ulog, key=key):
        assert click_more(ulog=ulog), key
        assert click(ulog=ulog, key="enter ultrasteadyvideo"), "enter ultrasteadyvideo"
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
    assert found(ulog=ulog, key=key), key

    return True


@file_validator(mime="mp4", quantity=1)
def take_ultrasteadyvideo(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))

    assert click_shutter(ulog=ulog)
    time.sleep(duration)
    assert click_shutter(ulog=ulog)
    # [enter]unstable uiautomator2
    for dummy in range(3):
        if found(ulog=ulog, key="leave ultrasteadyvideo") or found(ulog=ulog, key="enter album"):
            break
        assert click_shutter(ulog=ulog)
    # [leave]unstable uiautomator2

    # [enter][tuned]unstable uiautomator2
    time.sleep(3)
    # [leave][tuned]unstable uiautomator2

    return True


def teardown_ultrasteadyvideo(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    key = "leave ultrasteadyvideo"
    assert click(ulog=ulog, key=key), key
    return True
