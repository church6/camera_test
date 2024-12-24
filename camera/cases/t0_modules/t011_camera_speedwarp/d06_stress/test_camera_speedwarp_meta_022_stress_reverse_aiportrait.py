"""
# @filename    :  test_camera_speedwarp_meta_022_stress_reverse_aiportrait.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d06_stress.meta_022_stress_reverse_aiportrait import meta_do_speedwarp
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_SPEEDWARP


@pytest.mark.stress_speedwarp
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_SPEEDWARP))
@pytest.mark.skip_if_do_not_support_speedwarp()
def test_case_speedwarp_meta_022_stress_reverse_aiportrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_speedwarp(ulog=ulog)
    log.info("[leave]count=%d", count)
