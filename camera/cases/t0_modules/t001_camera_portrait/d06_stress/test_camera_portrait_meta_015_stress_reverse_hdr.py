"""
# @filename    :  test_camera_portrait_meta_015_stress_reverse_hdr.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d06_stress.meta_015_stress_reverse_hdr import meta_do_portrait
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PORTRAIT


@pytest.mark.stress_portrait
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_PORTRAIT))
def test_case_portrait_meta_015_stress_reverse_hdr(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_portrait(ulog=ulog)
    log.info("[leave]count=%d", count)
