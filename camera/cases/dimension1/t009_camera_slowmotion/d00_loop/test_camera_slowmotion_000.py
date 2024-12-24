"""
# @filename    :  test_camera_slowmotion_000.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d00_loop.meta_000_loop import meta_do_slowmotion
from camera.cases.dimension1.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_SLOWMOTION


@pytest.mark.dimension1
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_SLOWMOTION))
def test_case_slowmotion_meta_000_loop(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_slowmotion(ulog=ulog)
    log.info("[leave]count=%d", count)
