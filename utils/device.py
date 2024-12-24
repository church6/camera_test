"""
# @filename    :  device.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import List, Union
import adbutils


def get_device_list() -> List[str]:
    """
    Function :
    """
    # sanity check
    client = adbutils.AdbClient()
    # [enter]type hint for mypy
    devices: List[str] = [each.serial for each in client.list() if each.state == "device"]
    # [leave]type hint for mypy
    return devices


def device_is_online(serial_number: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    online = False
    client = adbutils.AdbClient()
    for each in client.list():
        if each.state != "device":
            continue
        if each.serial == serial_number:
            online = True
            break
    return online
