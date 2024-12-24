"""
# @filename    :  tombstone.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import Dict, Union
import os
import re
from datetime import datetime, timedelta
from utils.enums import EnumTombstone

TOMBSTONE_BASENAME_REGEX = re.compile(r"^tombstone_([\d]+)$")
TOMBSTONE_TIMESTAMP_REGEX = re.compile(
    r"^Timestamp: ([\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2}.[\d]{6})[\d]{3}[\+\-][\d]{4}$"
)
VENDOR_QTI_CAMERA_PROVIDER_BASENAME = "vendor.qti.camera.provider@2.7-service_64"
VENDOR_QTI_CAMERA_PROVIDER_FULLNAME = os.path.join("/vendor/bin/hw", VENDOR_QTI_CAMERA_PROVIDER_BASENAME)
TOMBSTONE_VENDOR_QTI_CAMERA_PROVIDER_REGEX = re.compile(rf"^Cmdline: ({re.escape(VENDOR_QTI_CAMERA_PROVIDER_FULLNAME)})$")
VENDOR_QTI_CAMERA_SERVER_BASENAME = "cameraserver"
VENDOR_QTI_CAMERA_SERVER_FULLNAME = os.path.join("/system/bin", VENDOR_QTI_CAMERA_SERVER_BASENAME)
TOMBSTONE_VENDOR_QTI_CAMERA_SERVER_REGEX = re.compile(rf"^Cmdline: ({re.escape(VENDOR_QTI_CAMERA_SERVER_FULLNAME)})$")


class TombstoneWorker:
    """
    Class :
    """

    def __init__(self, ulog=None, exception_timestamp: Union[str, None] = None, tombstone: Union[EnumTombstone, None] = None):
        """
        Function :
        """
        # pylint: disable=R0913
        # sanity check
        assert ulog is not None
        assert exception_timestamp is not None
        assert tombstone is not None
        self._ulog = ulog
        self._exception_timestamp = datetime.strptime(exception_timestamp, "%Y%m%d_%H%M%S")
        self._tombstone_type = tombstone
        self._screenshot_timestamp_dir = os.path.join(ulog.get_screenshot_directory(), exception_timestamp)
        assert os.path.exists(self._screenshot_timestamp_dir), self._screenshot_timestamp_dir
        self._tombstones_dir = os.path.join(self._screenshot_timestamp_dir, f"{exception_timestamp}_tombstones", "tombstones")
        self._tombstone_basename = None

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        if os.path.exists(self._tombstones_dir):
            self._tombstone_basename = self._find()
        else:
            log.info("%s: No such file or directory", self._tombstones_dir)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check

    def _get_tombstone_timestamp(self, filename: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert filename is not None
        timestamp, cmdline = None, None
        with open(file=filename, mode="r", encoding="utf-8", errors="ignore") as file:
            for line in file.readlines(4096):  # efficient 4096 bytes
                if timestamp is None:
                    matched = re.match(TOMBSTONE_TIMESTAMP_REGEX, line)
                    if matched:
                        # print(matched.groups())
                        timestamp = datetime.strptime(matched.groups()[0], "%Y-%m-%d %H:%M:%S.%f")
                        continue
                if cmdline is None:
                    if self._tombstone_type == EnumTombstone.TYPE_CAMERA_PROVIDER:
                        matched = re.match(TOMBSTONE_VENDOR_QTI_CAMERA_PROVIDER_REGEX, line)
                        if matched:
                            # print(matched.groups())
                            cmdline = matched.groups()[0]
                            break
                    elif self._tombstone_type == EnumTombstone.TYPE_CAMERA_SERVER:
                        matched = re.match(TOMBSTONE_VENDOR_QTI_CAMERA_SERVER_REGEX, line)
                        if matched:
                            # print(matched.groups())
                            cmdline = matched.groups()[0]
                            break
                    else:
                        pass
        # [enter]sanity check
        if cmdline is None:
            return None
        if not (
            self._exception_timestamp - timedelta(seconds=30) < timestamp < self._exception_timestamp + timedelta(seconds=30)
        ):
            return None
        # [leave]sanity check
        return timestamp

    def _find(self):
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        tombstone_basename = None
        tombstones_dict: Dict[datetime, str] = {}
        for entry in os.scandir(self._tombstones_dir):
            if entry.is_file(follow_symlinks=False):
                # print(entry.path)
                matched = re.match(TOMBSTONE_BASENAME_REGEX, entry.name)
                if not matched:
                    continue
                timestamp = self._get_tombstone_timestamp(str(entry.path))
                if timestamp is not None:
                    tombstones_dict[timestamp] = entry.name
                    # log.info("%s=%s", str(entry.name), timestamp)
                    continue

        if len(tombstones_dict) > 0:
            sorted_keys = list(sorted(tombstones_dict.keys(), reverse=True))
            tombstone_basename = tombstones_dict[sorted_keys[0]]
        log.info("tombstone=%s", tombstone_basename)
        return tombstone_basename

    def get_tombstone_basename(self):
        """
        Function :
        """
        # sanity check
        return self._tombstone_basename

    def read_tombstone_lines(self, max_count: int = 128):
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        if self._tombstone_basename is None:
            log.info(f"{self._tombstones_dir}: No tombstones")
            return None

        lines = []
        filename = os.path.join(self._tombstones_dir, self._tombstone_basename)
        with open(file=filename, mode="r", encoding="utf-8", errors="ignore") as file:
            for index, line in enumerate(file):
                if index == max_count:
                    break
                lines.append(line)
        return lines
