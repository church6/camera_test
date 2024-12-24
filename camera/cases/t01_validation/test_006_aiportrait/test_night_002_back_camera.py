"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import gc
import pytest
from utils.views import found
from camera.cases.t01_validation.test_006_aiportrait.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    doubt_portrait,
    set_zoom,
    restart_camera,
    set_reverse,
    set_aiportrait,
    setup_night,
    take_night,
    teardown_night,
)


@pytest.mark.aiportrait
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


@pytest.mark.aiportrait
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(16))
def test_case0_night(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_night(ulog=ulog)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
        if not found(ulog=ulog, key=each):
            continue
        assert set_zoom(ulog=ulog, mode=each)
        for each in ["ai portrait on", "ai portrait off"] * 3:
            ai_portrait_on = False
            if found(ulog=ulog, key="ai portrait on") or found(ulog=ulog, key="ai portrait off"):
                assert set_aiportrait(ulog=ulog, mode=each)
                if each == "ai portrait on":
                    ai_portrait_on = True
            assert take_night(ulog=ulog, reserved=False)
            assert doubt_portrait(ulog=ulog, expected=ai_portrait_on)
    assert teardown_night(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.aiportrait
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case1_night(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    for cycle_number in range(16):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter]cycle_number=%d", cycle_number)
        assert setup_night(ulog=ulog)
        assert set_reverse(ulog=ulog, camera="back camera")
        for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
            if not found(ulog=ulog, key=each):
                continue
            assert set_zoom(ulog=ulog, mode=each)
            for each in ["ai portrait on", "ai portrait off"] * 3:
                ai_portrait_on = False
                if found(ulog=ulog, key="ai portrait on") or found(ulog=ulog, key="ai portrait off"):
                    assert set_aiportrait(ulog=ulog, mode=each)
                    if each == "ai portrait on":
                        ai_portrait_on = True
                assert take_night(ulog=ulog, reserved=False)
                assert doubt_portrait(ulog=ulog, expected=ai_portrait_on)
        assert teardown_night(ulog=ulog)
        log.info("[leave]cycle_number=%d", cycle_number)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    log.info("[leave]count=%d", count)
