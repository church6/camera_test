"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import pytest
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW
from camera.cameras.hmd import (
    restart_camera,
    set_reverse,
    do_video,
    do_photo,
    do_portrait,
    do_night,
    do_burstshot,
    do_flashshot,
    do_dualsight,
    do_timelapse,
    do_panorama,
    do_slowmotion,
    do_professional,
    do_speedwarp,
    do_astrophoto,
    do_ultrasteadyvideo,
)
from camera.factors.internal0 import run_preview_monkey


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
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


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case00_video(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case01_photo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_photo(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case02_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_portrait(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case03_night(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_night(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case04_burstshot(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_burstshot(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case05_flashshot(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_flashshot(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case06_dualsight(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_dualsight(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case07_timelapse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_timelapse(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case08_panorama(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_panorama(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case09_slowmotion(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_slowmotion(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
def test_case10_professional(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_professional(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
@pytest.mark.skip_if_do_not_support_speedwarp()
def test_case11_speedwarp(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_speedwarp(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
@pytest.mark.skip_if_do_not_support_astrophoto()
def test_case12_astrophoto(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_astrophoto(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.preview
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PREVIEW))
@pytest.mark.skip_if_do_not_support_ultrasteadyvideo()
def test_case13_ultrasteadyvideo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert run_preview_monkey(ulog=ulog, cycle_number=8)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_ultrasteadyvideo(ulog=ulog)
    log.info("[leave]count=%d", count)
