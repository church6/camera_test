"""
# @filename    :  camera.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import Union
from utils.ulog import Ulog
from .base import (
    setup_video,
    take_video,
    teardown_video,
    setup_photo,
    take_photo,
    teardown_photo,
    setup_portrait,
    take_portrait,
    teardown_portrait,
    setup_night,
    take_night,
    teardown_night,
    setup_burstshot,
    take_burstshot,
    teardown_burstshot,
    setup_flashshot,
    take_flashshot,
    teardown_flashshot,
    setup_dualsight,
    take_dualsight,
    teardown_dualsight,
    setup_timelapse,
    take_timelapse,
    teardown_timelapse,
    setup_panorama,
    take_panorama,
    teardown_panorama,
    setup_slowmotion,
    take_slowmotion,
    teardown_slowmotion,
    setup_professional,
    take_professional,
    teardown_professional,
    setup_speedwarp,
    take_speedwarp,
    teardown_speedwarp,
    setup_astrophoto,
    take_astrophoto,
    teardown_astrophoto,
    setup_ultrasteadyvideo,
    take_ultrasteadyvideo,
    teardown_ultrasteadyvideo,
)


class CameraVideoWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_video(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_video(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_video(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_video(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraVideoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraPhotoWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_photo(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_photo(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_photo(ulog=self.ulog, reserved=reserved)
        return True


def do_photo(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraPhotoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraPortraitWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_portrait(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_portrait(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_portrait(ulog=self.ulog, reserved=reserved)
        return True


def do_portrait(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraPortraitWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraNightWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_night(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_night(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_night(ulog=self.ulog, reserved=reserved)
        return True


def do_night(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraNightWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraBurstshotWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_burstshot(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_burstshot(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_burstshot(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_burstshot(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraBurstshotWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraFlashshotWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_flashshot(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_flashshot(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_flashshot(ulog=self.ulog, reserved=reserved)
        return True


def do_flashshot(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraFlashshotWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraDualsightWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_dualsight(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_dualsight(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_dualsight(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_dualsight(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraDualsightWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraTimelapseWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_timelapse(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_timelapse(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_timelapse(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_timelapse(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraTimelapseWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraPanoramaWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_panorama(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_panorama(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_panorama(ulog=self.ulog, reserved=reserved)
        return True


def do_panorama(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraPanoramaWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraSlowmotionWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_slowmotion(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_slowmotion(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_slowmotion(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_slowmotion(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraSlowmotionWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraProfessionalWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_professional(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_professional(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_professional(ulog=self.ulog, reserved=reserved)
        return True


def do_professional(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraProfessionalWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraSpeedwarpWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_speedwarp(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_speedwarp(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_speedwarp(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_speedwarp(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraSpeedwarpWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


class CameraAstrophotoWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_astrophoto(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_astrophoto(ulog=self.ulog)

    def take(self, reserved: bool = False) -> bool:
        """
        Function :
        """
        assert take_astrophoto(ulog=self.ulog, reserved=reserved)
        return True


def do_astrophoto(ulog: Union[Ulog, None] = None, reserved: bool = False) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    with CameraAstrophotoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved)
    return True


class CameraUltrasteadyvideoWorker:
    """
    Class :
    """

    def __init__(self, ulog: Union[Ulog, None] = None):
        """
        Function :
        """
        # sanity check
        assert ulog is not None
        self.ulog = ulog

    def __enter__(self):
        """
        Function :
        """
        assert setup_ultrasteadyvideo(ulog=self.ulog)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Function :
        """
        assert teardown_ultrasteadyvideo(ulog=self.ulog)

    def take(self, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_ultrasteadyvideo(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def do_ultrasteadyvideo(ulog: Union[Ulog, None] = None, reserved: bool = False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraUltrasteadyvideoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True
