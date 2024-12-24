"""
# @filename    :  test_camera_video_003.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d01_zoom.meta_003_zoom_reverse import meta_do_video
from camera.cases.dimension2.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_VIDEO


@pytest.mark.dimension2
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_VIDEO))
def test_case_video_meta_003_zoom_reverse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_video(ulog=ulog)
    log.info("[leave]count=%d", count)
