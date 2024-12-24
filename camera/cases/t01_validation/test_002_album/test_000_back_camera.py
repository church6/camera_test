"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import pytest
from camera.cases.t01_validation.test_002_album.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import (
    restart_camera,
    set_reverse,
    do_night,
    do_portrait,
    do_photo,
    do_burstshot,
    do_flashshot,
    do_video,
    do_dualsight,
    do_timelapse,
    do_panorama,
    do_slowmotion,
    do_professional,
    do_speedwarp,
    do_astrophoto,
    do_ultrasteadyvideo,
    do_album_view,
    do_album_delete,
)


@pytest.mark.album
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


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case00_night(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_night(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case01_portrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_portrait(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case02_photo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_photo(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case03_burstshot(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_burstshot(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case04_flashshot(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_flashshot(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case05_video(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case06_dualsight(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_dualsight(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case07_timelapse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_timelapse(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case08_panorama(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_panorama(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case09_slowmotion(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_slowmotion(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case10_professional(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_professional(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
@pytest.mark.skip_if_do_not_support_speedwarp()
def test_case11_speedwarp(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_speedwarp(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
@pytest.mark.skip_if_do_not_support_astrophoto()
def test_case12_astrophoto(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_astrophoto(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.album
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
@pytest.mark.skip_if_do_not_support_ultrasteadyvideo()
def test_case13_ultrasteadyvideo(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_ultrasteadyvideo(ulog=ulog, reserved=True)
    assert do_album_view(ulog=ulog)
    assert do_album_delete(ulog=ulog)
    log.info("[leave]count=%d", count)
