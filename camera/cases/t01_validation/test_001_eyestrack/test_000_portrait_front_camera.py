"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import gc
import pytest
from camera.cases.t01_validation.test_001_eyestrack.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    restart_camera,
    set_reverse,
    do_portrait,
    toggle_dropdown_settings_by_key,  # only export for validation
)


@pytest.mark.eyestrack
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


@pytest.mark.eyestrack
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(64))
def test_case0_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=False)
    assert do_portrait(ulog=ulog)
    assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=True)
    log.info("[leave]count=%d", count)


@pytest.mark.eyestrack
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(64))
def test_case1_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=True)
    assert do_portrait(ulog=ulog)
    assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=False)
    log.info("[leave]count=%d", count)


@pytest.mark.eyestrack
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case2_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    for stress in range(64):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter][stress]%s", stress)
        assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=False)
        assert do_portrait(ulog=ulog)
        assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=True)
        log.info("[leave][stress]%s", stress)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    log.info("[leave]count=%d", count)


@pytest.mark.eyestrack
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case3_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    for stress in range(64):
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        log.info("[enter][stress]%s", stress)
        assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=True)
        assert do_portrait(ulog=ulog)
        assert toggle_dropdown_settings_by_key(ulog=ulog, key="eyes tracking toggle", enable=False)
        log.info("[leave][stress]%s", stress)
        # [enter][manually trigger garbage collection]
        log.info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
    log.info("[leave]count=%d", count)
