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
    setup_video,
    teardown_video,
    setup_photo,
    teardown_photo,
    setup_portrait,
    teardown_portrait,
    setup_night,
    teardown_night,
    setup_burstshot,
    teardown_burstshot,
    setup_flashshot,
    teardown_flashshot,
    setup_dualsight,
    teardown_dualsight,
    setup_timelapse,
    teardown_timelapse,
    setup_panorama,
    teardown_panorama,
    setup_slowmotion,
    teardown_slowmotion,
    setup_professional,
    teardown_professional,
    setup_speedwarp,
    teardown_speedwarp,
    setup_astrophoto,
    teardown_astrophoto,
    setup_ultrasteadyvideo,
    teardown_ultrasteadyvideo,
)

PREIVIEW_ACTIONS = [
    ("video", setup_video, teardown_video),
    ("photo", setup_photo, teardown_photo),
    ("portrait", setup_portrait, teardown_portrait),
    ("night", setup_night, teardown_night),
    ("burstshot", setup_burstshot, teardown_burstshot),
    ("flashshot", setup_flashshot, teardown_flashshot),
    ("dualsight", setup_dualsight, teardown_dualsight),
    ("timelapse", setup_timelapse, teardown_timelapse),
    ("panorama", setup_panorama, teardown_panorama),
    ("slowmotion", setup_slowmotion, teardown_slowmotion),
    ("professional", setup_professional, teardown_professional),
    ("speedwarp", setup_speedwarp, teardown_speedwarp),
    ("astrophoto", setup_astrophoto, teardown_astrophoto),
    ("ultrasteadyvideo", setup_ultrasteadyvideo, teardown_ultrasteadyvideo),
]


@retry(tries=6, delay=0.5, logger=None)
def do_preview_monkey(ulog: Union[Ulog, None] = None, index: int = 0) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert index is not None
    assert index in range(len(PREIVIEW_ACTIONS))
    module = PREIVIEW_ACTIONS[index][0]
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
    func0 = PREIVIEW_ACTIONS[index][1]
    assert func0(ulog=ulog), f"do_preview_monkey,{func0.__name__}"
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
    func1 = PREIVIEW_ACTIONS[index][2]
    assert func1(ulog=ulog), f"do_preview_monkey,{func1.__name__}"
    return True


def run_preview_monkey(ulog: Union[Ulog, None] = None, cycle_number: int = 3) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert cycle_number is not None
    assert cycle_number > 0
    log = ulog.get_camera_logger()
    array = list(range(len(PREIVIEW_ACTIONS))) * cycle_number
    random.shuffle(array)
    for index in array:
        log.info("[enter][%s][%s]", index, PREIVIEW_ACTIONS[index][0])
        assert do_preview_monkey(ulog=ulog, index=index)
        log.info("[leave][%s][%s]", index, PREIVIEW_ACTIONS[index][0])
    return True
