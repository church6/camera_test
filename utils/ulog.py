# pylint: disable=R0902
# pylint: disable=R0904
"""
# @filename    :  ulog.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
import stat
from typing import Any, Dict, Union
import datetime
import logging
import platform
import uiautomator2
from utils.run import run
from utils.constants import PYTEST_LOGS_DIRECTORY
from utils.enums import EnumDeviceChargeState
from utils.udev import Udev
from utils.ucam import Ucam
from utils.uenv import Uenv


class Singleton(type):
    """
    Class : it is NOT MT‐Safe.
    """

    # https://stackoverflow.com/questions/6760685
    _instances: Dict[Any, object] = {}

    def __call__(cls, *args, **kwargs):
        key: Union[object, str] = cls
        vector = []
        if any(args):
            vector.append("_".join(str(arg) for arg in args))
        if any(kwargs):
            vector.append("_".join(str(value) for value in kwargs.values()))
        if vector:
            # print(vector)
            key = "_".join(vector)
            # print(f"key = {key}")

        if key not in cls._instances:
            cls._instances[key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[key]


class Ulog(metaclass=Singleton):
    """
    Class :
    """

    def __init__(
        self, product_name: Union[str, None] = None, serial_number: Union[str, None] = None, timestamp: Union[str, None] = None
    ):
        """
        Function :
        """
        # print("__init__")
        # sanity check
        assert product_name is not None
        assert serial_number is not None
        assert timestamp is not None
        self._product_name = product_name
        self._serial_number = serial_number
        self._timestamp = timestamp
        self._device = uiautomator2.connect(serial_number)
        self._project_directory = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
        self._logs_directory = self._make_logs_directory()
        self._logger_directory = self._make_logger_directory()
        self._junit_filename = os.path.join(self._logger_directory, "pytest_junit.xml")
        self._report_html_filename = os.path.join(self._logger_directory, "pytest_report.html")
        self._allure_directory = self._make_logs_subdirectory("allure")
        self._allure_report_directory = self._make_logs_subdirectory("report")
        self._crash_directory = self._make_logs_subdirectory("pulled")
        self._logcat_directory = self._make_logs_subdirectory("logcat")
        self._shutter_directory = self._make_logs_subdirectory("shutter")
        self._screenshot_directory = self._make_logs_subdirectory("screenshot")
        self._appinfo_directory = self._make_logs_subdirectory("appinfo")
        self._sysinfo_directory = self._make_logs_subdirectory("sysinfo")
        self._logger_instances: Dict[str, Union[logging.Logger, None]] = {}
        self._logger_filenames: Dict[str, Union[str, None]] = {}
        self._camera_logger = self._make_pytest_logger("camera")
        # Make object 'Udev' a property member of class Ulog
        self._udev = Udev(product_name, serial_number, timestamp)
        # Make object 'Ucam' a property member of class Ulog
        self._ucam = Ucam(product_name, serial_number, timestamp)
        self._begin_timestamp = datetime.datetime.now()
        self._namespace_testnode_filename = None  # shared by multiprocessing
        self._namespace_testnode_funcname = None  # shared by multiprocessing
        self._shared_value1 = None  # indicate the status of device in charge
        # [enter][require Udev]
        self._allure_report_shell = self._make_allure_report_shell()
        # [leave][require Udev]
        self._log_gztar_shell = self._make_log_gztar_shell()
        env = Uenv(product_name, serial_number, timestamp)
        self._config_vertical_test_mode = env.get_bool_by_key(key="config_vertical_test_mode")

    def __str__(self) -> str:
        """
        Function :
        """
        return f"Ulog:{self._product_name},{self._serial_number},{self._timestamp}"

    def __repr__(self) -> str:
        """
        Function :
        """
        return f"Ulog:{self._product_name},{self._serial_number},{self._timestamp}"

    def init_testnode(self, namespace_testnode_filename, namespace_testnode_funcname):
        """
        Function :
        """
        self._namespace_testnode_filename = namespace_testnode_filename
        self._namespace_testnode_funcname = namespace_testnode_funcname

    def get_testnode(self):
        """
        Function :
        """
        assert self._namespace_testnode_filename is not None
        assert self._namespace_testnode_funcname is not None
        return (self._namespace_testnode_filename.shared_str, self._namespace_testnode_funcname.shared_str)

    def set_testnode(self, filename: Union[str, None] = None, funcname: Union[str, None] = None):
        """
        Function :
        """
        assert filename is not None
        assert funcname is not None
        self._namespace_testnode_filename.shared_str = filename
        self._namespace_testnode_funcname.shared_str = funcname

    def adb(self, command: Union[str, None] = None, block: bool = True, islog: bool = True):
        """
        Function :
        """
        assert command is not None
        get = run(rf"adb -s {self._serial_number} {command}", block=block)
        if islog:
            self.get_camera_logger().warning("%s = %s", command, get.status)
        return get

    def get_product_name(self) -> str:
        """
        Function :
        """
        return self._product_name

    def get_serial_number(self) -> str:
        """
        Function :
        """
        return self._serial_number

    def get_timestamp(self) -> str:
        """
        Function :
        """
        return self._timestamp

    def set_shared_value1(self, value=None):
        """
        Function :
        """
        assert value is not None
        self._shared_value1 = value

    def get_shared_number1(self):
        """
        Function :
        """
        assert self._shared_value1 is not None
        return self._shared_value1.value

    def set_shared_number1(self, number: Union[EnumDeviceChargeState, None] = None):
        """
        Function :
        """
        assert number is not None
        assert self._shared_value1 is not None
        self._shared_value1.value = number

    def is_day(self):
        """
        Function :
        """
        # use sun rise time and sun set time
        return 6 <= datetime.datetime.now().hour <= 19

    def is_dimlight(self):
        """
        Function :
        """
        # office is empty
        return 20 <= datetime.datetime.now().hour <= 6

    def is_night(self):
        """
        Function :
        """
        return not self.is_day()

    def get_device(self):
        """
        Function :
        """
        return self._device

    def get_display(self):
        """
        Function :
        """
        width, height = self._device.window_size()
        return (width, height)

    def get_project_directory(self) -> str:
        """
        Function :
        """
        return self._project_directory

    def get_logger_directory(self) -> str:
        """
        Function :
        """
        return self._logger_directory

    def get_junit_filename(self) -> str:
        """
        Function :
        """
        return self._junit_filename

    def get_report_html_filename(self) -> str:
        """
        Function :
        """
        return self._report_html_filename

    def get_allure_directory(self) -> str:
        """
        Function :
        """
        return self._allure_directory

    def get_allure_report_directory(self) -> str:
        """
        Function :
        """
        return self._allure_report_directory

    def get_allure_report_shell(self) -> str:
        """
        Function :
        """
        return self._allure_report_shell

    def get_log_gztar_shell(self) -> str:
        """
        Function :
        """
        return self._log_gztar_shell

    def get_crash_directory(self) -> str:
        """
        Function :
        """
        return self._crash_directory

    def get_logcat_directory(self) -> str:
        """
        Function :
        """
        return self._logcat_directory

    def get_shutter_directory(self) -> str:
        """
        Function :
        """
        return self._shutter_directory

    def get_screenshot_directory(self) -> str:
        """
        Function :
        """
        return self._screenshot_directory

    def get_appinfo_directory(self) -> str:
        """
        Function :
        """
        return self._appinfo_directory

    def get_sysinfo_directory(self) -> str:
        """
        Function :
        """
        return self._sysinfo_directory

    def get_logger_filename(self, name) -> Union[str, None]:
        """
        Function :
        """
        assert name is not None
        assert name != ""
        assert name in self._logger_filenames
        return self._logger_filenames[name]

    def get_logger(self, name):
        """
        Function :
        """
        assert name is not None
        assert name != ""
        assert name in self._logger_instances
        return self._logger_instances[name]

    def get_camera_logger(self):
        """
        Function :
        """
        return self._camera_logger

    def get_udev(self) -> Udev:
        """
        Function :
        """
        return self._udev

    def get_ucam(self) -> Ucam:
        """
        Function :
        """
        return self._ucam

    def get_begin_timestamp(self):
        """
        Function :
        """
        return self._begin_timestamp

    def _make_logs_directory(self):
        """
        Function :
        """
        # sanity check
        logs_directory = PYTEST_LOGS_DIRECTORY
        os.makedirs(logs_directory, exist_ok=True)
        return logs_directory

    def _make_logger_directory(self):
        """
        Function :
        """
        # sanity check
        logger_directory = os.path.join(self._logs_directory, f"pytest_{self._serial_number}_{self._timestamp}")
        os.makedirs(logger_directory, exist_ok=True)
        return logger_directory

    def _make_logs_subdirectory(self, name: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert name is not None
        assert name != ""
        subdirectory = os.path.join(self._logger_directory, name)
        os.makedirs(subdirectory, exist_ok=True)
        return subdirectory

    def _make_logger_filename(self, name: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert name is not None
        assert name != ""
        logger_filename: Union[str, None] = None
        if name in self._logger_filenames:
            logger_filename = self._logger_filenames[name]
        else:
            os.makedirs(os.path.join(self._logger_directory, name), exist_ok=True)
            logger_filename = os.path.join(self._logger_directory, name, "pytest.log")
            self._logger_filenames[name] = logger_filename
        return logger_filename

    def _make_console_logger(self, logger=None):
        """
        Function :
        """
        # sanity check
        assert logger is not None
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)06d %(levelno)2s %(name)s %(filename)s %(funcName)s %(lineno)4d %(message)s",
            datefmt="%Y-%02m-%02d %H:%M:%S",
        )
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)
        return logger

    def _make_file_logger(self, logger=None, name: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert logger is not None
        assert name is not None
        assert name != ""
        logger_filename = self._make_logger_filename(name)
        file_handler = logging.FileHandler(logger_filename)
        file_handler.setLevel(logging.DEBUG)
        log_formatter = logging.Formatter(
            fmt="%(asctime)s.%(msecs)06d %(levelno)2s %(name)s %(filename)s %(funcName)s %(lineno)4d %(message)s",
            datefmt="%Y-%02m-%02d %H:%M:%S",
        )
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
        return logger

    def _make_pytest_logger(self, name: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert name is not None
        assert name != ""
        logger: Union[logging.Logger, None] = None
        logger_filename = os.path.join(self._logger_directory, name, "pytest.log")
        # print(f"logger_filename = {logger_filename}")
        assert not os.path.exists(logger_filename)
        if not os.path.exists(logger_filename):
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
            logger = self._make_console_logger(logger)
            logger = self._make_file_logger(logger, name)
            self._logger_instances[name] = logger

        return logger

    def _make_allure_report_shell(self) -> str:
        """
        Function :
        """
        # sanity check
        platform_os = platform.system()
        assert platform_os in ["Darwin", "Linux", "Windows"]
        allure_binary_basename = "allure.bat" if platform_os == "Windows" else "allure"
        allure_binary_fullname = os.path.join(self._project_directory, "allure2_framework", "bin", allure_binary_basename)
        elements = [
            self._udev.get_product_boardname(),
            self._udev.get_hardware_version(),
            self._udev.get_ramsize(),
            self._udev.get_software_version(),
            self._serial_number,
            self._timestamp,
        ]
        allure_customized_name = " ".join(elements)
        # allure_report_default_fullname = os.path.join(self._allure_report_directory, "index.html")
        allure_report_modified_filename = f'index_{"_".join(elements)}_allure_report.html'
        # allure_report_modified_fullname = os.path.join(self._logger_directory, allure_report_modified_filename)
        filename = os.path.join(self._logger_directory, "allure_report.py")
        with open(file=filename, mode="w", encoding="utf-8") as file:
            file.write(
                rf'''#!/usr/bin/python3
"""
# @filename    :  allure_report.py
# @author      :  Copyright (C) Church.ZHONG
"""

import os
import shutil
import subprocess


def main():
    """
    Function :
    """
    # sanity check
    work_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(work_dir, "report", "index.html")
    dst = os.path.join(work_dir, "{allure_report_modified_filename}")
    if os.path.exists(dst):
        print(dst)
        return

    if not os.path.exists(src):
        command = [
            "{allure_binary_fullname}",
            "generate",
            os.path.join(work_dir, "allure"),
            "--single-file",
            "--output",
            os.path.join(work_dir, "report"),
            "--name",
            "'{allure_customized_name}'",
        ]
        subprocess.check_output(" ".join(command), shell=True)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
    else:
        print(f"{{src}}: No such file or directory")

    if not os.path.exists(dst):
        print(f"{{dst}}: No such file or directory")


if __name__ == "__main__":
    main()
'''
            )

        fstat = os.stat(filename)
        os.chmod(filename, fstat.st_mode | stat.S_IEXEC)
        return filename

    def _make_log_gztar_shell(self) -> str:
        """
        Function :
        """
        # pylint: disable=C0301
        # sanity check
        # [enter]make archive of logs after all processes finished.
        filename = os.path.join(self._logger_directory, "gztarlog.py")
        # [leave]make archive of logs after all processes finished.
        with open(file=filename, mode="w", encoding="utf-8") as file:
            file.write(
                r'''#!/usr/bin/python3
"""
# @filename    :  gztarlog.py
# @author      :  Copyright (C) Church.ZHONG
"""

import argparse
import os
import shutil


def main():
    """
    Function :
    """
    # sanity check
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", default=False, dest="all", help="all")
    parser.add_argument("-p", "--pulled", action="store_true", default=False, dest="pulled", help="pulled")
    parser.add_argument("-s", "--screenshot", action="store_true", default=False, dest="screenshot", help="screenshot")
    given = parser.parse_args()

    work_dir = os.path.dirname(os.path.abspath(__file__))
    work_dir_basename = os.path.basename(work_dir)
    if given.all:
        base_name = work_dir
        archive_name = f"{base_name}.tar.gz"
        if not os.path.exists(archive_name):
            shutil.make_archive(base_name=base_name, format="gztar", root_dir=work_dir, base_dir=".")
        if not os.path.exists(archive_name):
            print(f"{archive_name}: No such file or directory")

    if given.pulled:
        base_name = os.path.join(work_dir, f"{work_dir_basename}_pulled")
        archive_name = f"{base_name}.tar.gz"
        if not os.path.exists(archive_name):
            shutil.make_archive(base_name=base_name, format="gztar", root_dir=work_dir, base_dir="pulled")
        if not os.path.exists(archive_name):
            print(f"{archive_name}: No such file or directory")

    if given.screenshot:
        base_name = os.path.join(work_dir, f"{work_dir_basename}_screenshot")
        archive_name = f"{base_name}.tar.gz"
        if not os.path.exists(archive_name):
            shutil.make_archive(base_name=base_name, format="gztar", root_dir=work_dir, base_dir="screenshot")
        if not os.path.exists(archive_name):
            print(f"{archive_name}: No such file or directory")


if __name__ == "__main__":
    main()
'''
            )

        fstat = os.stat(filename)
        os.chmod(filename, fstat.st_mode | stat.S_IEXEC)
        return filename

    def get_config_vertical_test_mode(self) -> bool:
        """
        Function :
        """
        return self._config_vertical_test_mode
