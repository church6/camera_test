"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import pytest
from camera.cases.t01_validation.test_000_settings.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    restart_camera,
    set_reverse,
    do_timelapse,
    change_dropdown_settings,  # only export for validation
    change_global_settings,  # only export for validation
)


@pytest.mark.settings
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


@pytest.mark.settings
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case0_timelapse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    assert change_dropdown_settings(ulog=ulog, enable=False)
    assert change_global_settings(ulog=ulog)
    assert do_timelapse(ulog=ulog)
    assert change_dropdown_settings(ulog=ulog, enable=True)
    assert change_global_settings(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.settings
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case1_timelapse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="front camera")
    assert change_dropdown_settings(ulog=ulog, enable=True)
    assert change_global_settings(ulog=ulog)
    assert do_timelapse(ulog=ulog)
    assert change_dropdown_settings(ulog=ulog, enable=False)
    assert change_global_settings(ulog=ulog)
    log.info("[leave]count=%d", count)
