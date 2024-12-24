"""
# @filename    :  ucam.py
# @author      :  Copyright (C) Church.ZHONG
# @function    :  Make object 'Ucam' a property member of class Ulog
# @caution     :  DO NOT IMPORT ULOG
"""

from typing import Any, Dict, Union


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


class Ucam(metaclass=Singleton):
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
        self.reset_global_settings()

    def __str__(self) -> str:
        """
        Function :
        """
        return f"Ucam:{self._product_name},{self._serial_number},{self._timestamp}"

    def __repr__(self) -> str:
        """
        Function :
        """
        return f"Ucam:{self._product_name},{self._serial_number},{self._timestamp}"

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

    def reset_global_settings(self):
        """
        Function :
        """
        # sanity check
        # [enter]default value settings
        self._global_settings = {
            "shutter sound toggle": True,  # general
            "mirror front camera toggle": True,  # general
            "location tag toggle": True,  # general
            "haptic feedback toggle": True,  # general
            "brightness enhancement toggle": True,  # general
            "scan qrcode toggle": True,  # general
            "heif format toggle": False,  # general
            "ozo audio toggle": True,  # general
            "long press on shutter": False,  # photo
        }
        # [leave]default value settings

    def get_global_settings_keys(self):
        """
        Function :
        """
        # sanity check
        return list(self._global_settings.keys())

    def get_enabled_by_key(self, key: Union[str, None] = None) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key in self._global_settings
        return self._global_settings[key]

    def toggle_enabled_by_key(self, key: Union[str, None] = None):
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key in self._global_settings
        self._global_settings[key] = not self._global_settings[key]
