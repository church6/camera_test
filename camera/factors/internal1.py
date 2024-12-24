"""
# @filename    :  internal.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-08T16:09:59+08:00
"""

from typing import Union
import random
import time
from retry import retry
from utils.ulog import Ulog
from utils.features import get_variant_feature_by_product
from camera.cameras.hmd import (
    set_reverse,
    set_zoom,
    do_video,
    do_photo,
    do_portrait,
    do_night,
    do_burstshot,
    do_flashshot,
    do_dualsight,
    do_timelapse,
    do_panorama,
    do_slowmotion,
    do_professional,
    do_speedwarp,
    do_astrophoto,
    do_ultrasteadyvideo,
)

SHUTTERS_ACTIONS = [
    ("video", do_video, do_video),
    ("photo", do_photo, do_photo),
    ("portrait", do_portrait, do_portrait),
    ("night", do_night, do_night),
    ("burstshot", do_burstshot, do_burstshot),
    ("flashshot", do_flashshot, do_flashshot),
    ("dualsight", do_dualsight, do_dualsight),
    ("timelapse", do_timelapse, do_timelapse),
    ("panorama", do_panorama, do_panorama),
    ("slowmotion", do_slowmotion, do_slowmotion),
    ("professional", do_professional, do_professional),
    ("speedwarp", do_speedwarp, do_speedwarp),
    ("astrophoto", do_astrophoto, do_astrophoto),
    ("ultrasteadyvideo", do_ultrasteadyvideo, do_ultrasteadyvideo),
]


@retry(tries=6, delay=0.5, logger=None)
def do_shutters_monkey(ulog: Union[Ulog, None] = None, index: int = 0) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert index is not None
    assert index in range(len(SHUTTERS_ACTIONS))
    module = SHUTTERS_ACTIONS[index][0]
    log = ulog.get_camera_logger()
    camera_zoom_radios = get_variant_feature_by_product(ulog=ulog).CAMERA_ZOOM_RADIOS
    if module not in camera_zoom_radios:
        log.info("%s:not supported", module)
        return True
    features = []
    if module in camera_zoom_radios:
        capability = camera_zoom_radios[module]
        for value in capability.values():
            features.extend(value)
    func0 = SHUTTERS_ACTIONS[index][1]
    assert func0(ulog=ulog), f"do_shutters_monkey,{func0.__name__}"
    # [enter][tuned]wait to preview
    time.sleep(0.2)
    # [leave][tuned]wait to preview
    for camera in ["back camera", "front camera"]:
        log.info("[enter][%s][%s]", module, camera)
        assert set_reverse(ulog=ulog, camera=camera)
        for each in features * 2:
            if camera not in capability:
                continue
            if each not in capability[camera]:
                continue
            assert set_zoom(ulog=ulog, mode=each)
        log.info("[leave][%s][%s]", module, camera)
    func1 = SHUTTERS_ACTIONS[index][2]
    assert func1(ulog=ulog), f"do_shutters_monkey,{func1.__name__}"
    return True


def run_shutters_monkey(ulog: Union[Ulog, None] = None, cycle_number: int = 3) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert cycle_number is not None
    assert cycle_number > 0
    log = ulog.get_camera_logger()
    array = list(range(len(SHUTTERS_ACTIONS))) * cycle_number
    random.shuffle(array)
    for index in array:
        log.info("[enter][%s][%s]", index, SHUTTERS_ACTIONS[index][0])
        assert do_shutters_monkey(ulog=ulog, index=index)
        log.info("[leave][%s][%s]", index, SHUTTERS_ACTIONS[index][0])
    return True
