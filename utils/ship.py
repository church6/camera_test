"""
# @filename    :  ship.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import Union
from .run import run


def get_device_shipment(serial_number: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None

    get = run(f"adb -s {serial_number} shell getprop ro.vendor.build.shipment")
    if get.status and get.capture.strip() == "true":
        return True

    get = run(f"adb -s {serial_number} shell getprop ro.system.build.shipment")
    if get.status and get.capture.strip() == "true":
        return True

    return False
