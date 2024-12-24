"""
# @filename    :  test_camera_slowmotion_002.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_002_reverse_zoom import meta_do_slowmotion
from camera.cases.dimension2.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_SLOWMOTION


@pytest.mark.dimension2
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_SLOWMOTION))
def test_case_slowmotion_meta_002_reverse_zoom(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_slowmotion(ulog=ulog)
    log.info("[leave]count=%d", count)
