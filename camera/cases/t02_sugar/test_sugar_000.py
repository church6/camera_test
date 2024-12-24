"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import time
import pytest
from utils.features import get_node_by_key
from utils.views import found, click
from camera.cameras.hmd import restart_camera, set_reverse, setup_photo, teardown_photo

RATIOS = ["screen ratio 1:1", "screen ratio 4:3", "screen ratio 16:9", "screen ratio full"]


class DropdownSettingsWorker:
    """
    Class :
    """

    def __init__(self, ulog=None):
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
            time.sleep(0.5)
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key="more settings closed button"):
                assert click(ulog=self.ulog, key="more settings closed button")
            if found(ulog=self.ulog, key="more settings opened button"):
                break
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        # sanity check
        for dummy in range(3):
            # [enter][tuned]unstable uiautomator2
            time.sleep(0.5)
            # [leave][tuned]unstable uiautomator2
            if found(ulog=self.ulog, key="more settings opened button"):
                assert click(ulog=self.ulog, key="more settings opened button")
            if found(ulog=self.ulog, key="more settings closed button"):
                break

    def touch(self, key: int = 0) -> bool:
        """
        Function :
        """
        # sanity check
        assert key is not None
        log = self.ulog.get_camera_logger()
        device = self.ulog.get_device()
        node = get_node_by_key(ulog=self.ulog, key="legacy radio")
        elements = device(**node)
        if len(elements) > 0:
            elements[key].click()
            log.info("key=%s", key)
        else:
            if 0 <= key < len(RATIOS):
                if found(ulog=self.ulog, key=RATIOS[key]):
                    click(ulog=self.ulog, key=RATIOS[key])
                    log.info("key=%s", RATIOS[key])
            else:
                log.error("key=%s", key)
        return True


def set_dropdown_settings_by_key2(ulog=None, key: int = 0) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert key is not None
    with DropdownSettingsWorker(ulog=ulog) as worker:
        assert worker.touch(key)
    return True


@pytest.mark.sugar
@pytest.mark.parametrize("count", range(1))
def test_000_restart_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert restart_camera(ulog=ulog, clear=True)
    log.info("[leave]count=%d", count)


@pytest.mark.sugar
@pytest.mark.parametrize("count", range(1))
def test_case0_photo_whratio(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_photo(ulog=ulog)
    assert set_reverse(ulog=ulog, camera="back camera")
    node = get_node_by_key(ulog=ulog, key="shutter")
    device = ulog.get_device()
    for index in range(10240000):
        log.info("index=%s", index)
        for key in range(4):
            log.info("[enter]%s", key)
            assert set_dropdown_settings_by_key2(ulog=ulog, key=key)
            time.sleep(0.6)
            device(**node).click()
            ulog.adb("shell find /sdcard/DCIM/Camera -type f | xargs rm -rf")
            log.info("[leave]%s", key)
    assert teardown_photo(ulog=ulog)
    log.info("[leave]count=%d", count)
