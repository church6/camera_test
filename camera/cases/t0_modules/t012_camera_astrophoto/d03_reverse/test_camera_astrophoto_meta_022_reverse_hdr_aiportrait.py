"""
# @filename    :  test_camera_astrophoto_meta_022_reverse_hdr_aiportrait.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d03_reverse.meta_022_reverse_hdr_aiportrait import meta_do_astrophoto
from camera.cases.t0_modules.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_ASTROPHOTO


@pytest.mark.stress_astrophoto
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_MODULE_ASTROPHOTO))
@pytest.mark.skip_if_do_not_support_astrophoto()
def test_case_astrophoto_meta_022_reverse_hdr_aiportrait(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_astrophoto(ulog=ulog)
    log.info("[leave]count=%d", count)
