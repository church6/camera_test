"""
# @filename    :  test_camera_dualsight_000.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d00_loop.meta_000_loop import meta_do_dualsight
from camera.cases.dimension1.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_DUALSIGHT


@pytest.mark.dimension1
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_DUALSIGHT))
def test_case_dualsight_meta_000_loop(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_dualsight(ulog=ulog)
    log.info("[leave]count=%d", count)
