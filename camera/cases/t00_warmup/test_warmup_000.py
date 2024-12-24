"""
# @date        :  2024-04-08T16:09:59+08:00
"""

import pytest
from camera.cameras.hmd import warmup_camera


@pytest.mark.warmup
@pytest.mark.parametrize("count", range(1))
def test_000_warmup_camera(ulog, count):
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    log = ulog.get_camera_logger()
    log.info("[enter]count=%d", count)
    assert warmup_camera(ulog=ulog)
    log.info("[leave]count=%d", count)
