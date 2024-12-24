"""
# @filename    :  errors.py
# @author      :  Copyright (C) Church.ZHONG
# @caution     :  DO NOT IMPORT ULOG
"""

# [enter]DO NOT IMPORT ULOG
from typing import Union
from utils.enums import EnumException
from utils.features import get_variant_feature_by_product
from .handler import ExceptionHandler

# [leave]DO NOT IMPORT ULOG


class ExceptionDetector:
    """
    Class :
    """

    # pylint: disable=R0902
    def __init__(self, ulog=None, timestamp: Union[str, None] = None, witness: Union[str, None] = None, forced: bool = False):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        assert witness is not None
        assert witness != ""
        self._ulog = ulog
        self._timestamp = timestamp
        self._witness = witness
        self._forced = forced
        self._exception_type = EnumException.TYPE_NONE
        self._clazz = get_variant_feature_by_product(ulog=self._ulog)

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        self._exception_type = self._find_exception()
        if self._exception_type != EnumException.TYPE_NONE:
            # [enter]call ExceptionHandler via with statement
            with ExceptionHandler(
                ulog=self._ulog, timestamp=self._timestamp, witness=self._witness, exception_type=self._exception_type
            ) as handler:
                handler.process()
            # [leave]call ExceptionHandler via with statement
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        if self._exception_type != EnumException.TYPE_NONE:
            self._clean_exception()

    def _get_camera_app_pid(self) -> int:
        """
        Function :
        """
        # sanity check
        get = self._ulog.adb(command=f"shell pgrep -x -f {self._clazz.HMD_CAMERA_PACKAGE_NAME}", block=True, islog=False)
        pid = -1
        if get.status:
            try:
                pid = int(get.capture)
            except ValueError:
                pass
        return pid

    def _exception_is_camera_app_crash(self) -> bool:
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        key = self._witness
        if key not in self._clazz.NODES:
            return False
        node = self._clazz.NODES[key]
        if "packageName" not in node:
            return False
        if node["packageName"] != self._clazz.HMD_CAMERA_PACKAGE_NAME:
            return False
        pid = self._get_camera_app_pid()
        if pid < 0:
            log.error("[camera crash]%s", self._witness)
            return True
        return False

    def _exception_is_camera_app_error(self) -> bool:
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        device = self._ulog.get_device()
        # [enter][hard code]
        key = "camera error title"
        assert key in self._clazz.NODES
        node = self._clazz.NODES[key]
        if device(**node).exists():
            log.error("[camera error]%s", self._witness)
            return True
        # [leave][hard code]
        return False

    def _exception_is_anr(self) -> bool:
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        device = self._ulog.get_device()
        # [enter][hard code]
        key = "close app button"
        assert key in self._clazz.NODES
        node = self._clazz.NODES[key]
        if device(**node).exists():
            log.error("[anr]%s", self._witness)
            return True
        # [leave][hard code]
        return False

    def _exception_is_popup(self) -> bool:
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        device = self._ulog.get_device()
        current_package_name = device.app_current()["package"]
        if current_package_name not in [
            self._clazz.HMD_CAMERA_PACKAGE_NAME,
            self._clazz.HMD_ACTIVATION_PACKAGE_NAME,
            self._clazz.ANDROID_LAUNCHER3_PACKAGE_NAME,
            self._clazz.ANDROID_SETTINGS_PACKAGE_NAME,
            self._clazz.GOOGLE_PERMISSION_CONTROLLER_PACKAGE_NAME,
            self._clazz.GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        ]:
            log.error("[popup]%s,%s", current_package_name, self._witness)
            return True
        return False

    def _find_exception(self) -> int:
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        if self._forced:
            log.error("[forced error]%s", self._witness)
            return EnumException.TYPE_CAMERA_APP_ERROR
        if self._exception_is_camera_app_crash():
            return EnumException.TYPE_CAMERA_APP_CRASH
        if self._exception_is_camera_app_error():
            return EnumException.TYPE_CAMERA_APP_ERROR
        if self._exception_is_anr():
            return EnumException.TYPE_ANR
        if self._exception_is_popup():
            return EnumException.TYPE_POPUP
        return EnumException.TYPE_NONE

    def _clean_exception(self):
        """
        Function :
        """
        # sanity check
        device = self._ulog.get_device()
        # [enter]handle exception]
        with device.watch_context() as ctx:
            if self._exception_type == EnumException.TYPE_CAMERA_APP_ERROR:
                ctx.when("DISMISS").click()
            elif self._exception_type == EnumException.TYPE_ANR:
                ctx.when("Close app").click()
            elif self._exception_type == EnumException.TYPE_POPUP:
                ctx.when("Got it").click()
                ctx.when("CANCEL").click()
                current_package_name = device.app_current()["package"]
                if current_package_name != self._clazz.HMD_CAMERA_PACKAGE_NAME:
                    device.app_stop(current_package_name)
            else:
                pass
        # [leave][handle exception]

    def get_exception_type(self):
        """
        Function :
        """
        # sanity check
        return self._exception_type
