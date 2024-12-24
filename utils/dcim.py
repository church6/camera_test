# pylint: disable=R0902
"""
# @filename    :  dcim.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
from typing import List
from retry import retry
from utils.errors import catch_error

DCIM_FILE_EXTENTIONS = ("jpg", "mp4", "heif")


class CameraDirectoryWorker:
    """
    Class : https://stackoverflow.com/questions/17089728
    """

    def __init__(self, ulog=None, reserved=False, mime: str = "", quantity: int = 0, func_name: str = ""):
        """
        Function :
        """
        # pylint: disable=W0012
        # pylint: disable=R0913
        # pylint: disable=R0917
        # sanity check
        assert ulog is not None
        assert mime is not None
        assert mime in DCIM_FILE_EXTENTIONS
        assert quantity > 0
        assert func_name is not None
        assert func_name != ""
        self._ulog = ulog
        self._udev = ulog.get_udev()
        self._reserved = reserved
        self._mime = mime
        self._quantity = quantity
        self._func_name = func_name
        self._camera_dcim_directory = self._udev.get_camera_dcim_directory()
        self._filenames: List[str] = []

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        if not self._reserved:
            assert self._remove()

    def validate(self) -> bool:
        """
        Function : assert_eq(expected, actual)
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        # log.debug("func_name=%s", self._func_name)
        message = f"{self._func_name}(),reserved={self._reserved},mime={self._mime},expected={self._quantity}"
        if catch_error(ulog=self._ulog, witness=self._func_name, forced=False):
            # DO NOT return False here
            log.error("%s", message)

        # [enter][increase count]
        difference = self._find()
        increased = len(difference)
        log.info("increased=%d", increased)
        # [leave][increase count]

        # [enter][1st][RCA]
        assert increased != 0, f"{message},actual={increased}: increased != 0"
        # [leave][1st][RCA]
        # [enter][2nd]save files
        if self._udev.get_config_pull_dut_dcim_file():
            assert self._pull()
        # [leave][2nd]save files
        # [enter][3rd]check quantity of files
        if self._func_name == "take_burstshot":
            assert 0 < increased, f"{message},actual={increased}: 0 < increased"
        else:
            assert increased >= self._quantity, f"{message},actual={increased}: increased >= quantity"
        # [leave][3rd]check quantity of files

        if catch_error(ulog=self._ulog, witness=self._func_name, forced=False):
            # DO NOT return False here
            log.error("%s", message)

        return True

    @retry(tries=128, delay=0.5, logger=None)
    def _find(self) -> List[str]:
        """
        Function :
        """
        # sanity check
        message = f"{self._func_name}(),reserved={self._reserved},mime={self._mime},expected={self._quantity}"
        # [enter][Exclude hidden files]
        assert self._udev.adb("shell sync").status
        assert self._udev.adb("shell sync").status
        assert self._udev.adb("shell sync").status
        shell = f"shell \"find {self._camera_dcim_directory} -type f \\( -name '*.{self._mime}' -not -name '.*' \\)\""
        get = self._udev.adb(shell)
        # [leave][Exclude hidden files]
        assert get.status, message
        # [enter]type hint for mypy
        self._filenames = get.capture.splitlines()
        # [leave]type hint for mypy
        assert len(self._filenames) > 0, message
        return self._filenames

    @retry(tries=3, delay=0.5, logger=None)
    def _pull_one(self, src_filename=None, dst_filename=None) -> bool:
        """
        Function :
        """
        # sanity check
        assert src_filename is not None
        assert dst_filename is not None
        log = self._ulog.get_camera_logger()
        log.info("enter=%s", src_filename)
        assert self._udev.adb(f"pull {src_filename} {dst_filename}").status
        assert os.path.getsize(dst_filename) > 0
        log.info("leave=%s", src_filename)
        return True

    def _pull(self) -> bool:
        """
        Function :
        """
        # sanity check
        function_directory = os.path.join(self._ulog.get_shutter_directory(), self._func_name)
        if not os.path.exists(function_directory):
            os.makedirs(function_directory, exist_ok=True)

        for filename in self._filenames:
            src_filename = filename
            dst_filename = os.path.join(function_directory, os.path.basename(src_filename))
            assert self._pull_one(src_filename, dst_filename)
        return True

    @retry(tries=3, delay=0.5, logger=None)
    def _remove(self) -> bool:
        """
        Function :
        """
        # sanity check
        # [enter][remove subdirectory]
        assert self._udev.adb(f"shell rm -rf {self._camera_dcim_directory}/Burstshoot/IMG_*").status
        # [leave][remove subdirectory]
        # [enter][remove files]
        for filename in self._filenames:
            assert self._udev.adb(f"shell rm -f {filename}").status
        # [leave][remove files]
        return True


def do_validate(ulog=None, reserved=False, mime: str = "", quantity: int = 0, func_name: str = "") -> bool:
    """
    Function : assert_eq(expected, actual)
    """
    # pylint: disable=R0913
    # sanity check
    assert ulog is not None
    assert mime is not None
    assert mime in DCIM_FILE_EXTENTIONS
    assert quantity > 0
    assert func_name is not None
    assert func_name != ""
    with CameraDirectoryWorker(ulog=ulog, reserved=reserved, mime=mime, quantity=quantity, func_name=func_name) as worker:
        assert worker.validate()
    return True
