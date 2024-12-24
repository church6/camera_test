"""
# @filename    :  uenv.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import Any, Dict, Union
import os
import configparser
import platform
import pytest
from utils.constants import PYTEST_LOGS_DIRECTORY


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


class UenvImpl(metaclass=Singleton):
    """
    Class : like PImpl Idiom in C++
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
        self._section_name = f"{product_name}_{serial_number}_{timestamp}"
        self._config = configparser.ConfigParser()
        self._allure_directory = os.path.join(PYTEST_LOGS_DIRECTORY, f"pytest_{serial_number}_{timestamp}", "allure")
        self._config_fullname = self._make_env_file("environment.properties")

    def __str__(self) -> str:
        """
        Function :
        """
        return f"UenvImpl:{self._product_name},{self._serial_number},{self._timestamp}"

    def __repr__(self) -> str:
        """
        Function :
        """
        return f"UenvImpl:{self._product_name},{self._serial_number},{self._timestamp}"

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        self._config.read(self._config_fullname, encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        with open(file=self._config_fullname, mode="w", encoding="utf-8") as cfile:
            self._config.write(cfile)

    def _make_env_file(self, name: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert name is not None
        assert name != ""
        os.makedirs(self._allure_directory, exist_ok=True)
        filename = os.path.join(self._allure_directory, name)
        self._config.add_section(self._section_name)
        self._config.set(self._section_name, "python", platform.python_version())
        self._config.set(self._section_name, "pytest", pytest.__version__)
        self._config.set(self._section_name, "product_name", self._product_name)
        self._config.set(self._section_name, "serial_number", self._serial_number)
        self._config.set(self._section_name, "timestamp", self._timestamp)
        with open(file=filename, mode="w", encoding="utf-8") as cfile:
            self._config.write(cfile)
        return filename

    def get_bool_by_key(self, key: Union[str, None] = None) -> Union[bool, None]:
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key != ""
        if key not in dict(self._config.items(self._section_name)):
            return None
        return self._config.getboolean(self._section_name, key)

    def get_int_by_key(self, key: Union[str, None] = None) -> Union[int, None]:
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key != ""
        if key not in dict(self._config.items(self._section_name)):
            return None
        return self._config.getint(self._section_name, key)

    def get_env_by_key(self, key: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key != ""
        if key not in dict(self._config.items(self._section_name)):
            return None
        return self._config.get(self._section_name, key)

    def set_env_by_key(self, key: Union[str, None] = None, value: Union[bool, str, None] = None) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key != ""
        assert value is not None
        done = False
        try:
            self._config.set(self._section_name, key, str(value))
            done = True
        except configparser.NoSectionError:
            pass
        assert done, f"{key}={value}"
        return True


class Uenv:
    """
    Class :
    """

    def __init__(
        self, product_name: Union[str, None] = None, serial_number: Union[str, None] = None, timestamp: Union[str, None] = None
    ):
        """
        Function :
        """
        # sanity check
        assert product_name is not None
        assert serial_number is not None
        assert timestamp is not None
        self._product_name = product_name
        self._serial_number = serial_number
        self._timestamp = timestamp

    def __str__(self) -> str:
        """
        Function :
        """
        return f"Uenv:{self._product_name},{self._serial_number},{self._timestamp}"

    def __repr__(self) -> str:
        """
        Function :
        """
        return f"Uenv:{self._product_name},{self._serial_number},{self._timestamp}"

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

    def get_bool_by_key(self, key: Union[str, None] = None) -> Union[bool, None]:
        """
        Function :
        """
        # sanity check
        assert key is not None
        value = None
        with UenvImpl(self._product_name, self._serial_number, self._timestamp) as env:
            value = env.get_bool_by_key(key=key)
        return value

    def get_int_by_key(self, key: Union[str, None] = None) -> Union[int, None]:
        """
        Function :
        """
        # sanity check
        assert key is not None
        value = None
        with UenvImpl(self._product_name, self._serial_number, self._timestamp) as env:
            value = env.get_int_by_key(key=key)
        return value

    def get_env_by_key(self, key: Union[str, None] = None) -> Any:
        """
        Function :
        """
        # sanity check
        assert key is not None
        value = None
        with UenvImpl(self._product_name, self._serial_number, self._timestamp) as env:
            value = env.get_env_by_key(key=key)
        return value

    def set_env_by_key(self, key: Union[str, None] = None, value: Union[bool, str, None] = None):
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert value is not None
        with UenvImpl(self._product_name, self._serial_number, self._timestamp) as env:
            assert env.set_env_by_key(key=key, value=value)
        return True
