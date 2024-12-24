"""
# @filename    :  views.py
# @author      :  Copyright (C) Church.ZHONG
# @function    :  run uiautomator2 with less but important logging
"""

from typing import Union
import time
from utils.tryui import tryui
from utils.ulog import Ulog
from utils.features import get_node_by_key


@tryui
def fetch(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    return device(**node)


@tryui
def information(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    return device(**node).info


@tryui
def get_text(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50) -> Union[str, None]:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    return device(**node).get_text()


@tryui
def found(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50, assured: bool = False) -> bool:
    """
    Function :
    """
    # pylint: disable=W0613
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    return device(**node).exists()


@tryui
def click(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    device(**node).click()

    return True


@tryui
def long_click(ulog: Union[Ulog, None] = None, key: str = "", noop: int = 50, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    assert key != ""
    # pylint: disable=R1716
    assert 0 <= noop and noop < 1000, f"noop={noop}"
    assert duration > 0

    # [enter]unstable uiautomator2
    if noop > 0:
        time.sleep(noop / 1000)
    # [leave]unstable uiautomator2

    node = get_node_by_key(ulog=ulog, key=key)
    device = ulog.get_device()
    device(**node).long_click(duration=duration)

    return True
