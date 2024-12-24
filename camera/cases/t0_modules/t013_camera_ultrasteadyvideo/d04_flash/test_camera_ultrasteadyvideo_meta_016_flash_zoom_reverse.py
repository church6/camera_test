"""
# @filename    :  test_camera_ultrasteadyvideo_meta_016_flash_zoom_reverse.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d04_flash.meta_016_flash_zoom_reverse import meta_do_ultrasteadyvideo
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_ULTRASTEADYVIDEO


@pytest.mark.stress_ultrasteadyvideo
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_ULTRASTEADYVIDEO))
@pytest.mark.skip_if_do_not_support_ultrasteadyvideo()
def test_case_ultrasteadyvideo_meta_016_flash_zoom_reverse(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_ultrasteadyvideo(ulog=ulog)
    log.info("[leave]count=%d", count)
