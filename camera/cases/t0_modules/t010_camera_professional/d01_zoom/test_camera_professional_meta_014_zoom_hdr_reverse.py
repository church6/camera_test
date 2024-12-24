"""
# @filename    :  test_camera_professional_meta_014_zoom_hdr_reverse.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d01_zoom.meta_014_zoom_hdr_reverse import meta_do_professional
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PROFESSIONAL


@pytest.mark.stress_professional
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PROFESSIONAL))
def test_case_professional_meta_014_zoom_hdr_reverse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_professional(ulog=ulog)
    log.info("[leave]count=%d", count)
