"""
# @filename    :  album.py
# @author      :  Copyright (C) Church.ZHONG
"""

import time
from typing import Union
from utils.ulog import Ulog
from utils.views import found, click


################################################################
# define actions of album module
################################################################
class AlbumWorker:
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

    def __enter__(self):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "enter album"
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key="leave album"):
                break
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "leave album"
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key="shutter"):
                break

    def view(self) -> bool:
        """
        Function :
        """
        # sanity check
        return True

    def delete(self) -> bool:
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.2)
            # [leave][tuned]unstable uiautomator2
            key = "album more options"
            if found(ulog=self.ulog, key=key):
                assert click(ulog=self.ulog, key=key), key
                break
        ################################################################
        time.sleep(0.2)
        key = "album delete from device"
        assert click(ulog=self.ulog, key=key), key
        ################################################################
        ################################################################
        time.sleep(0.2)
        key = "album delete all 5 photos confirm"
        if found(ulog=self.ulog, key=key):
            assert click(ulog=self.ulog, key=key), key
        ################################################################
        ################################################################
        time.sleep(0.2)
        key = "album delete from device confirm"
        if found(ulog=self.ulog, key=key):
            assert click(ulog=self.ulog, key=key), key
        ################################################################
        return True


def do_album_view(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with AlbumWorker(ulog=ulog) as worker:
        assert worker.view()
    return True


def do_album_delete(ulog: Union[Ulog, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with AlbumWorker(ulog=ulog) as worker:
        assert worker.delete()
    return True
