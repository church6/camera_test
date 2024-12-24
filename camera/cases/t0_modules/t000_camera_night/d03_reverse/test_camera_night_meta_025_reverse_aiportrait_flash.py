"""
# @filename    :  test_camera_night_meta_025_reverse_aiportrait_flash.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_025_reverse_aiportrait_flash import meta_do_night
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_NIGHT


@pytest.mark.stress_night
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_NIGHT))
def test_case_night_meta_025_reverse_aiportrait_flash(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_night(ulog=ulog)
    log.info("[leave]count=%d", count)
