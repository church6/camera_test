# pylint: disable=R0902
"""
# @filename    :  udev.py
# @author      :  Copyright (C) Church.ZHONG
# @function    :  Make object 'Udev' a property member of class Ulog
# @caution     :  DO NOT IMPORT ULOG
"""

# DO NOT IMPORT ULOG#
import os
from typing import Any, Dict, Union
from utils.constants import DUT_CAMERA_TEST_ADB_DIRECTORY, DUT_CAMERA_TEST_DCIM_DIRECTORY, DUT_CAMERA_TEST_QUIT_INDICATOR_FILE
from utils.run import run
from utils.ship import get_device_shipment
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


class Udev(metaclass=Singleton):
    """
    Class :
    """

    def __init__(
        self, product_name: Union[str, None] = None, serial_number: Union[str, None] = None, timestamp: Union[str, None] = None
    ):
        """
        Function :
        """
        # pylint: disable=W0238
        # print("__init__")
        # sanity check
        assert product_name is not None
        assert serial_number is not None
        assert timestamp is not None
        self._product_name = product_name
        self._serial_number = serial_number
        self._timestamp = timestamp
        self._project_directory = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
        self._ramsize = self.adb("shell getprop ro.boot.config.ramsize").capture
        self._sys_locale = self.adb("shell getprop persist.sys.locale").capture
        self._software_version = self.adb("shell getprop ro.build.software.version").capture
        self._product_boardname = self.adb("shell getprop ro.product.board").capture
        self._hardware_version = self.adb("shell getprop ro.boot.hardware.revision").capture
        self._software_shipment = get_device_shipment(serial_number)
        self._camera_dcim_directory = self._make_camera_dcim_directory()
        self._camera_test_directory = self._make_camera_test_directory()
        env = Uenv(product_name, serial_number, timestamp)
        self._config_pull_dut_dcim_file = env.get_bool_by_key(key="config_pull_dut_dcim_file")
        # [enter][add some environment variables into test report]
        env.set_env_by_key(key="software_shipment", value=str(self._software_shipment))
        env.set_env_by_key(key="ram_size", value=self._ramsize)
        env.set_env_by_key(key="software_version", value=self._software_version)
        env.set_env_by_key(key="product_boardname", value=self._product_boardname)
        env.set_env_by_key(key="hardware_version", value=self._hardware_version)
        # [leave][add some environment variables into test report]

    def __str__(self) -> str:
        """
        Function :
        """
        return f"Udev:{self._product_name},{self._serial_number},{self._timestamp}"

    def __repr__(self) -> str:
        """
        Function :
        """
        return f"Udev:{self._product_name},{self._serial_number},{self._timestamp}"

    def adb(self, command: Union[str, None] = None):
        """
        Function :
        """
        assert command is not None
        return run(rf"adb -s {self._serial_number} {command}")

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

    def get_ramsize(self) -> str:
        """
        Function :
        """
        return self._ramsize

    def get_sys_locale(self) -> str:
        """
        Function :
        """
        return self._sys_locale

    def get_software_version(self) -> str:
        """
        Function :
        """
        return self._software_version

    def get_product_boardname(self) -> str:
        """
        Function :
        """
        return self._product_boardname

    def get_hardware_version(self) -> str:
        """
        Function :
        """
        return self._hardware_version

    def get_software_shipment(self) -> bool:
        """
        Function :
        """
        return self._software_shipment

    def get_battery_capacity(self) -> int:
        """
        Function :
        """
        capacity = 0
        for dummy in range(3):
            get = self.adb("shell cmd battery get level")
            if get.status:
                capacity = int(get.capture)
                break
            get = self.adb("shell cmd battery reset -f")
            assert get.status
            get = self.adb("shell cmd battery unplug -f")
            assert get.status
        return capacity

    def get_camera_dcim_directory(self) -> str:
        """
        Function :
        """
        return self._camera_dcim_directory

    def get_camera_test_directory(self) -> str:
        """
        Function :
        """
        return self._camera_test_directory

    def get_config_pull_dut_dcim_file(self) -> bool:
        """
        Function :
        """
        return self._config_pull_dut_dcim_file

    def get_camera_test_quit_indicator(self) -> bool:
        """
        Function :
        """
        return self.adb(f"shell test -f {DUT_CAMERA_TEST_QUIT_INDICATOR_FILE}").status

    def _make_camera_dcim_directory(self) -> str:
        """
        Function :
        """
        # sanity check
        camera_dcim_directory = DUT_CAMERA_TEST_DCIM_DIRECTORY
        assert self.adb(f"shell mkdir -p {camera_dcim_directory}").status
        return camera_dcim_directory

    def _make_camera_test_directory(self) -> str:
        """
        Function :
        """
        # sanity check
        camera_test_directory = DUT_CAMERA_TEST_ADB_DIRECTORY
        assert self.adb(f"shell mkdir -p {camera_test_directory}").status
        return camera_test_directory
