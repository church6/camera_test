"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import gc
import pytest
from utils.views import found
from camera.cases.t01_validation.test_004_qrcode.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    doubt_qrcode,
    set_zoom,
    restart_camera,
    set_reverse,
    setup_photo,
    take_photo,
    teardown_photo,
    setup_portrait,
    teardown_portrait,
)


@pytest.mark.qrcode
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
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


@pytest.mark.qrcode
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(8))
def test_case0_photo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_photo(ulog=ulog)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
        if not found(ulog=ulog, key=each):
            continue
        assert set_zoom(ulog=ulog, mode=each)
        assert take_photo(ulog=ulog, reserved=False)
        assert doubt_qrcode(ulog=ulog, expected=True)
    assert teardown_photo(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.qrcode
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case1_photo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    for cycle_number in range(8):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter]cycle_number=%d", cycle_number)
        assert setup_photo(ulog=ulog)
        assert set_reverse(ulog=ulog, camera="back camera")
        for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
            if not found(ulog=ulog, key=each):
                continue
            assert set_zoom(ulog=ulog, mode=each)
            assert take_photo(ulog=ulog, reserved=False)
            assert doubt_qrcode(ulog=ulog, expected=True)
        assert teardown_photo(ulog=ulog)
        assert setup_portrait(ulog=ulog)
        assert teardown_portrait(ulog=ulog)
        log.info("[leave]cycle_number=%d", cycle_number)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    log.info("[leave]count=%d", count)
