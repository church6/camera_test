"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import pytest
from camera.cases.t01_validation.test_00a_digital_zoom.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER
from camera.cameras.hmd import restart_camera, set_zoom, set_hdr, set_flash, set_aiportrait, set_reverse, do_professional, set_pinchout, set_pinchin


@pytest.mark.digital_zoom
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


@pytest.mark.digital_zoom
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case00_professional_zoom(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["zoom 0.5", "zoom 1", "zoom 2", "zoom 3", "zoom 4"] * 3:
        assert set_zoom(ulog=ulog, mode=each)
        assert do_professional(ulog=ulog, reserved=False)
        assert set_pinchout(ulog=ulog)
        assert set_pinchin(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.digital_zoom
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case01_professional_hdr(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["hdr auto", "hdr on", "hdr off"] * 3:
        assert set_hdr(ulog=ulog, mode=each)
        assert do_professional(ulog=ulog, reserved=False)
        assert set_pinchout(ulog=ulog)
        assert set_pinchin(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.digital_zoom
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case02_professional_flash(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["flash auto", "flash on", "flash off"] * 3:
        assert set_flash(ulog=ulog, mode=each)
        assert do_professional(ulog=ulog, reserved=False)
        assert set_pinchout(ulog=ulog)
        assert set_pinchin(ulog=ulog)
    log.info("[leave]count=%d", count)


@pytest.mark.digital_zoom
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER))
def test_case03_professional_aiportrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert set_reverse(ulog=ulog, camera="back camera")
    for each in ["ai portrait on", "ai portrait off"] * 3:
        assert set_aiportrait(ulog=ulog, mode=each)
        assert do_professional(ulog=ulog, reserved=False)
        assert set_pinchout(ulog=ulog)
        assert set_pinchin(ulog=ulog)
    log.info("[leave]count=%d", count)
