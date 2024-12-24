"""
# @filename    :  test_camera_panorama_meta_015_reverse_hdr_zoom.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_015_reverse_hdr_zoom import meta_do_panorama
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PANORAMA


@pytest.mark.stress_panorama
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PANORAMA))
def test_case_panorama_meta_015_reverse_hdr_zoom(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_panorama(ulog=ulog)
    log.info("[leave]count=%d", count)
