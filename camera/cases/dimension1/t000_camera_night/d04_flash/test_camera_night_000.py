"""
# @filename    :  test_camera_night_000.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-17T14:26:11+08:00
"""

import pytest
from camera.metas.d04_flash.meta_000_flash import meta_do_night
from camera.cases.dimension1.constants import PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_NIGHT


@pytest.mark.dimension1
# @pytest.mark.skip(reason="church")
@pytest.mark.parametrize("count", range(PYTEST_MARK_PARAMETRIZE_MAXIMUM_RANGE_NUMBER_OF_DIMENSION1_NIGHT))
def test_case_night_meta_000_flash(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert meta_do_night(ulog=ulog)
    log.info("[leave]count=%d", count)
