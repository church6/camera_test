"""
# @filename    :  test_camera_video_durability_000_back_camera.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.cameras.hmd import set_reverse, do_video


@pytest.mark.stress_video
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1, 30))
def test_case0_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, duration=count)
    log.info("[leave]count=%d", count)


@pytest.mark.stress_video
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1))
def test_case1_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, duration=120)
    log.info("[leave]count=%d", count)


@pytest.mark.stress_video
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1))
def test_case2_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, duration=600)
    log.info("[leave]count=%d", count)


@pytest.mark.stress_video
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1))
def test_case3_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, duration=1200)
    log.info("[leave]count=%d", count)


@pytest.mark.stress_video
@pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1))
def test_case4_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    assert do_video(ulog=ulog, duration=1800)
    log.info("[leave]count=%d", count)


@pytest.mark.stress_video
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(1))
def test_case5_video_back_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    for duration in range(1, 30):
        assert do_video(ulog=ulog, duration=duration)
    log.info("[leave]count=%d", count)
