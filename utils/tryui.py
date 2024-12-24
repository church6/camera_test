"""
# @filename    :  tryui.py
# @author      :  Copyright (C) Church.ZHONG
"""

import functools
import utils

DICT_FN_DEFAULT_RETURN_VALUES = {
    "fetch": None,
    "information": None,
    "get_text": None,
    "found": False,
    "click": False,
    "long_click": False,
}


def tryui(func):
    """
    Function : decorator
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Function :
        """
        # sanity check
        assert "ulog" in kwargs
        assert "key" in kwargs
        ulog, key = kwargs["ulog"], kwargs["key"]
        assert ulog is not None
        assert key is not None
        log = ulog.get_camera_logger()

        assert func.__name__ in DICT_FN_DEFAULT_RETURN_VALUES
        value = DICT_FN_DEFAULT_RETURN_VALUES[func.__name__]
        forced_error = False
        try:
            value = func(*args, **kwargs)
        except Exception:  # pylint: disable=W0718
            log.error('%s(ulog=ulog, key="%s")', func.__name__, key)
            # [enter][condition1]forced_error=True
            if func.__name__ in ["click", "long_click"]:
                forced_error = True
            # [leave][condition1]forced_error=True
        finally:
            # [enter][condition2]forced_error=True
            if func.__name__ == "found" and "assured" in kwargs:
                assured = kwargs["assured"]
                if value != assured:
                    log.error('found(ulog=ulog, key="%s")', key)
                    forced_error = True
            else:
                # do something in the future
                pass
            # [leave][condition2]forced_error=True

            if utils.errors.catch_error(ulog=ulog, witness=key, forced=forced_error):
                value = DICT_FN_DEFAULT_RETURN_VALUES[func.__name__]

        return value

    return wrapper
