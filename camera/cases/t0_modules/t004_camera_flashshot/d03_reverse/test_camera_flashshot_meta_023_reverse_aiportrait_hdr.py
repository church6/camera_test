"""
# @filename    :  test_camera_flashshot_meta_023_reverse_aiportrait_hdr.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_023_reverse_aiportrait_hdr import meta_do_flashshot
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_FLASHSHOT


@pytest.mark.stress_flashshot
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_FLASHSHOT))
def test_case_flashshot_meta_023_reverse_aiportrait_hdr(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_flashshot(ulog=ulog)
    log.info("[leave]count=%d", count)
