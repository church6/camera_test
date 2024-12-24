"""
# @filename    :  test_camera_slowmotion_meta_017_aiportrait_reverse_zoom.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d05_aiportrait.meta_017_aiportrait_reverse_zoom import meta_do_slowmotion
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_SLOWMOTION


@pytest.mark.stress_slowmotion
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_SLOWMOTION))
def test_case_slowmotion_meta_017_aiportrait_reverse_zoom(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_slowmotion(ulog=ulog)
    log.info("[leave]count=%d", count)
