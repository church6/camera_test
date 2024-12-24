"""
# @filename    :  test_camera_ultrasteadyvideo_001.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d01_zoom.meta_001_zoom_loop import meta_do_ultrasteadyvideo
from camera.cases.dimension2.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_ULTRASTEADYVIDEO


@pytest.mark.dimension2
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION2_ULTRASTEADYVIDEO))
@pytest.mark.skip_if_do_not_support_ultrasteadyvideo()
def test_case_ultrasteadyvideo_meta_001_zoom_loop(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_ultrasteadyvideo(ulog=ulog)
    log.info("[leave]count=%d", count)
