"""
# @filename    :  errors.py
# @author      :  Copyright (C) Church.ZHONG
# @caution     :  DO NOT IMPORT ULOG
"""

# [enter]DO NOT IMPORT ULOG
import os
from typing import Union
from pathlib import Path
from retry import retry
from utils.enums import EnumTombstone, EnumException
from utils.constants import PROJECT_ROOT_DIRECTORY
from .tombstone import TombstoneWorker

# [leave]DO NOT IMPORT ULOG


class ExceptionHandler:
    """
    Class :
    """

    # pylint: disable=R0902
    def __init__(
        self,
        ulog=None,
        timestamp: Union[str, None] = None,
        witness: Union[str, None] = None,
        exception_type: Union[EnumException, None] = None,
    ):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        assert witness is not None
        assert witness != ""
        self._ulog = ulog
        self._witness = witness
        self._exception_type = exception_type
        # [enter][testnode]
        testnode_filename, testnode_funcname = self._ulog.get_testnode()
        self._relative_testnode_filename = os.path.relpath(testnode_filename, PROJECT_ROOT_DIRECTORY)
        self._testnode_filename = str(testnode_filename).replace(" ", "_")
        self._testnode_funcname = str(testnode_funcname).replace(" ", "_")
        # [leave][testnode]
        self._exception_timestamp = timestamp
        # [enter][local directory name]
        self._timestamp_screenshot_dir = os.path.join(self._ulog.get_screenshot_directory(), self._exception_timestamp)
        self._timestamp_bugreport_dir = os.path.join(self._timestamp_screenshot_dir, f"{self._exception_timestamp}_bugreport")
        self._timestamp_hmdlogs_dir = os.path.join(self._timestamp_screenshot_dir, f"{self._exception_timestamp}_hmdlogs")
        self._timestamp_tombstones_dir = os.path.join(self._timestamp_screenshot_dir, f"{self._exception_timestamp}_tombstones")
        self._timestamp_stemname = f"{self._exception_timestamp}_{Path(self._testnode_filename).stem}_{self._testnode_funcname}"
        # [leave][local directory name]
        # [enter][local exception file name]
        self._exception_bugreport_file = os.path.join(self._timestamp_bugreport_dir, f"{self._timestamp_stemname}.html")
        self._exception_dumpsys_file = os.path.join(self._timestamp_bugreport_dir, f"{self._timestamp_stemname}.dump")
        self._exception_screenshot_file = os.path.join(self._timestamp_bugreport_dir, f"{self._timestamp_stemname}.png")
        # [leave][local exception file name]

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        os.makedirs(self._timestamp_bugreport_dir, exist_ok=True)
        os.makedirs(self._timestamp_hmdlogs_dir, exist_ok=True)
        os.makedirs(self._timestamp_tombstones_dir, exist_ok=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check

    @retry(tries=3, delay=0.5, logger=None)
    def _save_screenshot(self):
        """
        Function :
        """
        # sanity check
        # log.info("enter")
        log = self._ulog.get_camera_logger()
        device = self._ulog.get_device()
        screenshot_src_file = os.path.join("/sdcard/Documents", f"{self._timestamp_stemname}.png")
        device.screen_on()
        assert self._ulog.adb(f"shell /system/bin/screencap -p {screenshot_src_file}").status
        assert self._ulog.adb(f"pull {screenshot_src_file} {self._exception_screenshot_file}").status
        assert os.path.exists(self._exception_screenshot_file)
        assert os.path.getsize(self._exception_screenshot_file) > 0
        assert self._ulog.adb(f"shell rm -f {screenshot_src_file}").status
        log.error("screenshot:%s", self._exception_screenshot_file)
        # log.info("leave")

    def _save_dumpsys(self):
        """
        Function :
        """
        # sanity check
        # [enter]dumpsys media.camera
        with open(file=self._exception_dumpsys_file, mode="w", encoding="utf-8") as file:
            file.write("[enter]dumpsys media.camera\n")
            get = self._ulog.adb("shell dumpsys media.camera")
            file.write(get.capture)
            file.write("[leave]dumpsys media.camera\n")

            file.write("[enter]dumpsys media.camera.proxy\n")
            get = self._ulog.adb("shell dumpsys media.camera.proxy")
            file.write(get.capture)
            file.write("[leave]dumpsys media.camera.proxy\n")
        # [leave]dumpsys media.camera

    def _save_logs(self):
        """
        Function :
        """
        # sanity check
        log = self._ulog.get_camera_logger()
        # [enter][pull tombstones]
        get = self._ulog.adb(f"pull /data/tombstones {self._timestamp_tombstones_dir}")
        log.info(f"pull /data/tombstones {self._timestamp_tombstones_dir} = {get.status}")
        # [leave][pull tombstones]

        # [enter][pull hmdlogs]
        get = self._ulog.adb('shell find /data/local/hmdlogs/aplog -maxdepth 1 -type f -name "kernel_*" | sort -r | head -n 6')
        for each in get.capture.splitlines():
            self._ulog.adb(command=f"pull {each} {self._timestamp_hmdlogs_dir}", block=True, islog=False)
        get = self._ulog.adb('shell find /data/local/hmdlogs/aplog -maxdepth 1 -type f -name "logcat_*" | sort -r | head -n 6')
        for each in get.capture.splitlines():
            self._ulog.adb(command=f"pull {each} {self._timestamp_hmdlogs_dir}", block=True, islog=False)
        # [leave][pull hmdlogs]

    def _save_bugreport(self):
        """
        Function :
        """
        # pylint: disable=C0301
        # sanity check
        log = self._ulog.get_camera_logger()
        tombstone_a_tags = []
        tombstone_text = ""
        for tombstone in (EnumTombstone.TYPE_CAMERA_PROVIDER, EnumTombstone.TYPE_CAMERA_SERVER):
            # [enter]read tombstones
            tombstone_basename, tombstone_lines = None, None
            with TombstoneWorker(ulog=self._ulog, exception_timestamp=self._exception_timestamp, tombstone=tombstone) as worker:
                tombstone_basename, tombstone_lines = worker.get_tombstone_basename(), worker.read_tombstone_lines()
                tombstone_text += "N/A" if not tombstone_lines else "".join(tombstone_lines)
                tombstone_text += "\n"
            # [leave]read tombstones
            # [enter][pull tombstones]
            if tombstone_basename:
                get = self._ulog.adb(f"pull /data/tombstones/{tombstone_basename} {self._timestamp_bugreport_dir}")
                log.info(f"pull /data/tombstones/{tombstone_basename} {self._timestamp_bugreport_dir} = {get.status}")
                tombstone_a_tags.append(
                    rf"""<a target="_blank" href="{tombstone_basename}"><div> {tombstone_basename} </div></a>"""
                )
            # [leave][pull tombstones]

        # [enter]write bugreport
        html = []
        html.append(rf"""<tr><td>exception_tombstone</td><td> {"".join(tombstone_a_tags)} </td></tr>""")
        if os.path.exists(self._exception_screenshot_file):
            html.append(
                rf"""<tr><td>exception_screenshot</td><td><a target="_blank" href="{self._timestamp_stemname}.png"><div> screenshot </div></a></td></tr>"""
            )
        if os.path.exists(self._exception_dumpsys_file):
            html.append(
                rf"""<tr><td>exception_dumpsys</td><td><a target="_blank" href="{self._timestamp_stemname}.dump"><div> dumpsys media.camera </div></a></td></tr>"""
            )
        innerhtml = "\n".join(html)
        with open(file=self._exception_bugreport_file, mode="w", encoding="utf-8") as file:
            file.write(
                rf"""<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>bug report</title>
<style>
.tombstone {{color:gray; white-space:normal; font-size:16px; text-align:left; white-space: pre-wrap; word-wrap:break-word;}}
</style>
</head>
<body>
<div align="center">
<h1>bug report</h1>

<table>
<tr><td>product_boardname</td><td> {self._ulog.get_udev().get_product_boardname()} </td></tr>
<tr><td>hardware_version</td><td> {self._ulog.get_udev().get_hardware_version()} </td></tr>
<tr><td>ramsize</td><td> {self._ulog.get_udev().get_ramsize()} </td></tr>
<tr><td>software_version</td><td> {self._ulog.get_udev().get_software_version()} </td></tr>
<tr><td>serial_number</td><td> {self._ulog.get_serial_number()} </td></tr>
<tr><td>pytest_begin_timestamp</td><td> {self._ulog.get_timestamp()} </td></tr>
<tr><td>testnode_filename</td><td>
<a target="_blank" href="http://gerrit.hmdglobal.com:8080/r/plugins/gitiles/tools/tools-sys/+/refs/heads/master/camera_test/{self._relative_testnode_filename}">
<div> {self._relative_testnode_filename} </div>
</a>
</td></tr>
<tr><td>testnode_funcname</td><td> {self._testnode_funcname} </td></tr>

<!--
<tr><td>Bug Title</td><td> N/A </td></tr>
<tr><td>Environment</td><td> N/A </td></tr>
<tr><td>Steps to Reproduce</td><td> N/A </td></tr>
<tr><td>Expected Result</td><td> N/A </td></tr>
<tr><td>Actual Result</td><td> N/A </td></tr>
<tr><td>Visual Proof (screenshots, videos, text)</td><td> N/A </td></tr>
<tr><td>Severity/Priority</td><td> Critical/High </td></tr>
-->

<tr><td>exception_witness</td><td style="color:#FF0000"> {self._witness} </td></tr>
<tr><td>exception_timestamp</td><td style="color:#FF0000"> {self._exception_timestamp} </td></tr>
<tr><td>exception_type</td><td style="color:#FF0000"> {self._exception_type.name} </td></tr>
{innerhtml}
</table>

<div class="tombstone"> {tombstone_text} </div>
</div>
</body>
</html>
"""
            )
        # [leave]write bugreport

    def process(self) -> bool:
        """
        Function :
        """
        # sanity check
        # [enter][1st]dumpsys media.camera
        if self._exception_type in [EnumException.TYPE_CAMERA_APP_CRASH, EnumException.TYPE_CAMERA_APP_ERROR]:
            self._save_dumpsys()
        # [leave][1st]dumpsys media.camera

        # [enter][2nd][save screenshot for all exceptions]
        self._save_screenshot()
        # [leave][2nd][save screenshot for all exceptions]

        # [enter][3rd][save logs]
        if self._exception_type in [EnumException.TYPE_CAMERA_APP_CRASH, EnumException.TYPE_CAMERA_APP_ERROR]:
            self._save_logs()
        # [leave][3rd][save logs]

        # [enter][4th][bug report]
        self._save_bugreport()
        # [leave][4th][bug report]
        return True
