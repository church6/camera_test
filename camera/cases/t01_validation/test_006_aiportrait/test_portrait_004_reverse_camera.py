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
    setup_portrait,
    take_portrait,
    teardown_portrait,
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
def test_case0_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_portrait(ulog=ulog)
    for camera in ["back camera", "front camera"] * 3:
        assert set_reverse(ulog=ulog, camera=camera)
        assert set_aiportrait(ulog=ulog, mode="ai portrait on")
        for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
            if not found(ulog=ulog, key=each):
                continue
            assert set_zoom(ulog=ulog, mode=each)
            assert take_portrait(ulog=ulog, reserved=False)
            expected = camera == "back camera"
            assert doubt_portrait(ulog=ulog, expected=expected)
    assert teardown_portrait(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.aiportrait
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case1_portrait(ulog, count):
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
        assert setup_portrait(ulog=ulog)
        for camera in ["back camera", "front camera"] * 3:
            assert set_reverse(ulog=ulog, camera=camera)
            assert set_aiportrait(ulog=ulog, mode="ai portrait on")
            for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
                if not found(ulog=ulog, key=each):
                    continue
                assert set_zoom(ulog=ulog, mode=each)
                assert take_portrait(ulog=ulog, reserved=False)
                expected = camera == "back camera"
                assert doubt_portrait(ulog=ulog, expected=expected)
        assert teardown_portrait(ulog=ulog)
        log.info("[leave]cycle_number=%d", cycle_number)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    log.info("[leave]count=%d", count)
