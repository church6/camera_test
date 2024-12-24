"""
# @filename    :  test_camera_dualsight_meta_014_hdr_zoom_reverse.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d02_hdr.meta_014_hdr_zoom_reverse import meta_do_dualsight
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_DUALSIGHT


@pytest.mark.stress_dualsight
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_DUALSIGHT))
def test_case_dualsight_meta_014_hdr_zoom_reverse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_dualsight(ulog=ulog)
    log.info("[leave]count=%d", count)
