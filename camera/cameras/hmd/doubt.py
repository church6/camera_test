"""
# @filename    :  doubt.py
# @author      :  Copyright (C) Church.ZHONG
"""

import time
from typing import Union
from retry import retry
from utils.ulog import Ulog
from utils.views import found, click
from .base import toggle_scan_qrcode, set_flash, click_center


class Facader:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog
        self.try_torch_on = bool(self.ulog.is_night() or found(ulog=self.ulog, key="try night mode"))

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        if self.try_torch_on:
            set_flash(ulog=self.ulog, mode="torch on")
        # [enter][tuned]wait to preview
        time.sleep(0.5)
        # [leave][tuned]wait to preview
        if found(ulog=self.ulog, key="save network menu"):
            assert click(ulog=self.ulog, key="save network button")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        if self.try_torch_on:
            set_flash(ulog=self.ulog, mode="flash auto")

    @retry(tries=3, delay=0.5, jitter=0.5, logger=None)
    def validate(self, key: str = "", expected: bool = False) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        assert key != ""
        assert click_center(ulog=self.ulog)
        assert found(ulog=self.ulog, key=key, assured=expected) is expected, f"key={key},expected={expected}"
        return True


def doubt_qrcode(ulog: Union[Ulog, None] = None, expected: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert toggle_scan_qrcode(ulog=ulog, enable=True)
    with Facader(ulog=ulog) as facader:
        assert facader.validate(key="qrcode action text", expected=expected)
    return True


def doubt_portrait(ulog: Union[Ulog, None] = None, expected: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert toggle_scan_qrcode(ulog=ulog, enable=False)
    with Facader(ulog=ulog) as facader:
        assert facader.validate(key="try portrait mode", expected=expected)
    return True
