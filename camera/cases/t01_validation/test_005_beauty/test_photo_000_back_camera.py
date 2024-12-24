"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import gc
import pytest
from utils.views import found
from camera.cases.t01_validation.test_005_beauty.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    click_center,
    restart_camera,
    toggle_scan_qrcode,
    set_reverse,
    set_beauty,
    set_zoom,
    setup_photo,
    take_photo,
    teardown_photo,
    set_pinchout,
    set_pinchin,
)


@pytest.mark.beauty
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


@pytest.mark.beauty
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(16))
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
        assert toggle_scan_qrcode(ulog=ulog, enable=False)
        for mode in ["default", "beauty mode", "skintone natural mode", "skintone bright mode"] * 3:
            assert set_beauty(ulog=ulog, mode=mode)
            assert take_photo(ulog=ulog, reserved=False)
            assert set_pinchout(ulog=ulog)
            assert set_pinchin(ulog=ulog)
            assert take_photo(ulog=ulog, reserved=False)
            assert click_center(ulog=ulog)
    assert teardown_photo(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.beauty
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
    assert setup_photo(ulog=ulog)
    for cycle_number in range(16):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter]cycle_number=%d", cycle_number)
        assert set_reverse(ulog=ulog, camera="back camera")
        for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
            if not found(ulog=ulog, key=each):
                continue
            assert set_zoom(ulog=ulog, mode=each)
            assert toggle_scan_qrcode(ulog=ulog, enable=False)
            for mode in ["default", "beauty mode", "skintone natural mode", "skintone bright mode"] * 3:
                assert set_beauty(ulog=ulog, mode=mode)
                assert take_photo(ulog=ulog, reserved=False)
                assert set_pinchout(ulog=ulog)
                assert set_pinchin(ulog=ulog)
                assert take_photo(ulog=ulog, reserved=False)
                assert click_center(ulog=ulog)
        log.info("[leave]cycle_number=%d", cycle_number)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    assert teardown_photo(ulog=ulog)
    log.info("[leave]count=%d", count)
