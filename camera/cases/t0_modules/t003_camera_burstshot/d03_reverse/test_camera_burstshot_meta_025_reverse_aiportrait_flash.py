"""
# @filename    :  test_camera_burstshot_meta_025_reverse_aiportrait_flash.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_025_reverse_aiportrait_flash import meta_do_burstshot
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_BURSTSHOT


@pytest.mark.stress_burstshot
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_BURSTSHOT))
def test_case_burstshot_meta_025_reverse_aiportrait_flash(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_burstshot(ulog=ulog)
    log.info("[leave]count=%d", count)
