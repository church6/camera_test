"""
# @filename    :  meta_085_zoom_aiportrait_flash_reverse.py
# @author      :  Copyright (C) Church.ZHONG
"""

from typing import Union
from utils.ulog import Ulog
from camera.cameras.hmd import (
    setup_night,
    take_night,
    teardown_night,
    setup_portrait,
    take_portrait,
    teardown_portrait,
    setup_photo,
    take_photo,
    teardown_photo,
    setup_video,
    take_video,
    teardown_video,
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
from camera.metas.constants import (
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_VIDEO,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_PHOTO,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_PORTRAIT,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_NIGHT,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_BURSTSHOT,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_FLASHSHOT,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_DUALSIGHT,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_TIMELAPSE,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_PANORAMA,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_SLOWMOTION,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_SPEEDWARP,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO,
    META_ZOOM_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_VIDEO,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_PHOTO,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_PORTRAIT,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_NIGHT,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_BURSTSHOT,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_FLASHSHOT,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_DUALSIGHT,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_TIMELAPSE,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_PANORAMA,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_SLOWMOTION,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_SPEEDWARP,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO,
    META_REVERSE_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_VIDEO,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_PHOTO,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_PORTRAIT,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_NIGHT,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_BURSTSHOT,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_FLASHSHOT,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_DUALSIGHT,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_TIMELAPSE,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_PANORAMA,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_SLOWMOTION,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_SPEEDWARP,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO,
    META_FLASH_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_VIDEO,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PHOTO,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PORTRAIT,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_NIGHT,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_BURSTSHOT,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_FLASHSHOT,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_DUALSIGHT,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_TIMELAPSE,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PANORAMA,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_SLOWMOTION,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_SPEEDWARP,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO,
    META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO,
)
from camera.metas.decorators import zoom, reverse, flash, aiportrait


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_NIGHT)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_NIGHT)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_NIGHT)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_NIGHT)
def take_night_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_night(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_night_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_night(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraNightWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_PORTRAIT)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PORTRAIT)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_PORTRAIT)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_PORTRAIT)
def take_portrait_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_portrait(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_portrait_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_portrait(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraPortraitWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_PHOTO)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PHOTO)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_PHOTO)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_PHOTO)
def take_photo_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_photo(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_photo_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_photo(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraPhotoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_VIDEO)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_VIDEO)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_VIDEO)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_VIDEO)
def take_video_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_video(ulog=ulog, reserved=reserved, duration=duration)
    return True


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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_video_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_video(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_BURSTSHOT)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_BURSTSHOT)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_BURSTSHOT)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_BURSTSHOT)
def take_burstshot_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_burstshot(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_burstshot_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_burstshot(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_FLASHSHOT)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_FLASHSHOT)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_FLASHSHOT)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_FLASHSHOT)
def take_flashshot_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_flashshot(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_flashshot_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_flashshot(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraFlashshotWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_DUALSIGHT)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_DUALSIGHT)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_DUALSIGHT)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_DUALSIGHT)
def take_dualsight_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_dualsight(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_dualsight_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_dualsight(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_TIMELAPSE)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_TIMELAPSE)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_TIMELAPSE)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_TIMELAPSE)
def take_timelapse_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_timelapse(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_timelapse_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_timelapse(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_PANORAMA)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PANORAMA)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_PANORAMA)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_PANORAMA)
def take_panorama_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_panorama(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_panorama_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_panorama(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraPanoramaWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_SLOWMOTION)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_SLOWMOTION)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_SLOWMOTION)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_SLOWMOTION)
def take_slowmotion_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_slowmotion(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_slowmotion_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_slowmotion(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_PROFESSIONAL)
def take_professional_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_professional(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_professional_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_professional(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraProfessionalWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_SPEEDWARP)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_SPEEDWARP)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_SPEEDWARP)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_SPEEDWARP)
def take_speedwarp_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_speedwarp(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_speedwarp_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_speedwarp(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_ASTROPHOTO)
def take_astrophoto_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_astrophoto(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_astrophoto_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_astrophoto(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert 0 < duration
    assert isinstance(duration, (float, int))
    with CameraAstrophotoWorker(ulog=ulog) as worker:
        assert worker.take(reserved=reserved, duration=duration)
    return True


@zoom(cycle_number=META_ZOOM_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO)
@aiportrait(cycle_number=META_AIPORTRAIT_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO)
@flash(cycle_number=META_FLASH_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO)
@reverse(cycle_number=META_REVERSE_MAXIMUM_CYCLE_NUMBER_ULTRASTEADYVIDEO)
def take_ultrasteadyvideo_wrapper(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
    """
    Function :
    """
    # sanity check
    assert ulog is not None
    assert take_ultrasteadyvideo(ulog=ulog, reserved=reserved, duration=duration)
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

    def take(self, reserved=False, duration: Union[float, int] = 1.5) -> bool:
        """
        Function :
        """
        assert take_ultrasteadyvideo_wrapper(ulog=self.ulog, reserved=reserved, duration=duration)
        return True


def meta_do_ultrasteadyvideo(ulog: Union[Ulog, None] = None, reserved=False, duration: Union[float, int] = 1.5) -> bool:
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
