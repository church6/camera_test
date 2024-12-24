"""
# @filename    :  decorators.py
# @author      :  Copyright (C) Church.ZHONG
"""

import gc
import functools
from camera.cameras.hmd import get_reverse, set_zoom, set_hdr, set_reverse, set_flash, set_aiportrait
from utils.features import get_variant_feature_by_product


def loop(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def loop_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            log.info("[enter][loop]%s", func.__name__)
            for each in range(cycle_number):
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                log.info("[enter]%s:%d", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%d", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][loop]%s", func.__name__)
            return True

        return wrapper

    return loop_wrapper


def zoom(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def zoom_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            camera_zoom_radios = get_variant_feature_by_product(ulog=ulog).CAMERA_ZOOM_RADIOS
            module = None
            for key in camera_zoom_radios:
                if key in func.__name__:
                    module = key
                    break
            assert module is not None
            log.info("[enter][zoom]%s", func.__name__)
            capability = camera_zoom_radios[module]
            features = []
            for value in capability.values():
                features.extend(value)
            for each in features * cycle_number:
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                camera = get_reverse(ulog=ulog)
                if camera in capability and each in capability[camera]:
                    assert set_zoom(ulog=ulog, mode=each)
                log.info("[enter]%s:%s", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%s", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][zoom]%s", func.__name__)
            return True

        return wrapper

    return zoom_wrapper


def hdr(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def hdr_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            camera_hdr_modes = get_variant_feature_by_product(ulog=ulog).CAMERA_HDR_MODES
            module = None
            for key in camera_hdr_modes:
                if key in func.__name__:
                    module = key
                    break
            assert module is not None
            log.info("[enter][hdr]%s", func.__name__)
            capability = camera_hdr_modes[module]
            features = []
            for value in capability.values():
                features.extend(value)
            for each in features * cycle_number:
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                camera = get_reverse(ulog=ulog)
                if camera in capability and each in capability[camera]:
                    assert set_hdr(ulog=ulog, mode=each)
                log.info("[enter]%s:%s", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%s", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][hdr]%s", func.__name__)
            return True

        return wrapper

    return hdr_wrapper


def reverse(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def reverse_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            status = True
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            camera_claim = get_variant_feature_by_product(ulog=ulog).CAMERA_CLAIM
            log.info("[enter][reverse]%s", func.__name__)
            for each in camera_claim * cycle_number:
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                log.info("[enter]%s:%s", func.__name__, each)
                assert set_reverse(ulog=ulog, camera=each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%s", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][reverse]%s", func.__name__)
            return status

        return wrapper

    return reverse_wrapper


def flash(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def flash_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            camera_flash_modes = get_variant_feature_by_product(ulog=ulog).CAMERA_FLASH_MODES
            module = None
            for key in camera_flash_modes:
                if key in func.__name__:
                    module = key
                    break
            assert module is not None
            log.info("[enter][flash]%s", func.__name__)
            capability = camera_flash_modes[module]
            features = []
            for value in capability.values():
                features.extend(value)
            for each in features * cycle_number:
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                camera = get_reverse(ulog=ulog)
                if camera in capability and each in capability[camera]:
                    assert set_flash(ulog=ulog, mode=each)
                log.info("[enter]%s:%s", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%s", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][flash]%s", func.__name__)
            return True

        return wrapper

    return flash_wrapper


def aiportrait(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def aiportrait_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            camera_aiportrait_modes = get_variant_feature_by_product(ulog=ulog).CAMERA_AIPORTRAIT_MODES
            module = None
            for key in camera_aiportrait_modes:
                if key in func.__name__:
                    module = key
                    break
            assert module is not None
            log.info("[enter][aiportrait]%s", func.__name__)
            capability = camera_aiportrait_modes[module]
            features = []
            for value in capability.values():
                features.extend(value)
            for each in features * cycle_number:
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                camera = get_reverse(ulog=ulog)
                if camera in capability and each in capability[camera]:
                    assert set_aiportrait(ulog=ulog, mode=each)
                log.info("[enter]%s:%s", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%s", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][aiportrait]%s", func.__name__)
            return True

        return wrapper

    return aiportrait_wrapper


def stress(cycle_number=2):
    """
    Function : decorator
    """
    assert cycle_number > 0

    def stress_wrapper(func):
        """
        Function :
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Function :
            """
            # sanity check
            assert "ulog" in kwargs
            ulog = kwargs["ulog"]
            log = ulog.get_camera_logger()
            log.info("[enter][stress]%s", func.__name__)
            for each in range(cycle_number):
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
                log.info("[enter]%s:%d", func.__name__, each)
                assert func(*args, **kwargs)
                log.info("[leave]%s:%d", func.__name__, each)
                # [enter][manually trigger garbage collection]
                log.info("collected=%s", gc.collect())
                # [leave][manually trigger garbage collection]
            log.info("[leave][stress]%s", func.__name__)
            return True

        return wrapper

    return stress_wrapper
