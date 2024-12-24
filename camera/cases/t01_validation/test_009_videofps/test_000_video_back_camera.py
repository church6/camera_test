"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import gc
import pytest
from utils.views import found
from camera.cases.t01_validation.test_009_videofps.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    restart_camera,
    set_reverse,
    set_dropdown_settings_by_key,
    set_zoom,
    setup_video,
    take_video,
    teardown_video,
)


@pytest.mark.videofps
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


@pytest.mark.videofps
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(3))
def test_case0_video(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_video(ulog=ulog)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
        if not found(ulog=ulog, key=each):
            continue
        assert set_zoom(ulog=ulog, mode=each)
        for resolution in ["video setting 1080p", "video setting 4k"] * 3:
            for fps in ["video setting 30fps", "video setting 60fps"] * 3:
                assert set_dropdown_settings_by_key(ulog=ulog, key=resolution)
                assert set_dropdown_settings_by_key(ulog=ulog, key=fps)
                assert take_video(ulog=ulog, reserved=False)
    assert teardown_video(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.videofps
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case1_video(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert setup_video(ulog=ulog)
    for cycle_number in range(3):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter]cycle_number=%d", cycle_number)
        assert set_reverse(ulog=ulog, camera="back camera")
        for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
            if not found(ulog=ulog, key=each):
                continue
            assert set_zoom(ulog=ulog, mode=each)
            for resolution in ["video setting 1080p", "video setting 4k"] * 3:
                for fps in ["video setting 30fps", "video setting 60fps"] * 3:
                    assert set_dropdown_settings_by_key(ulog=ulog, key=resolution)
                    assert set_dropdown_settings_by_key(ulog=ulog, key=fps)
                    assert take_video(ulog=ulog, reserved=False)
        log.info("[leave]cycle_number=%d", cycle_number)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    assert teardown_video(ulog=ulog)
    log.info("[leave]count=%d", count)
