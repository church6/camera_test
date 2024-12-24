#!/usr/bin/python3
"""
# @filename    :  run.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-22T10:37:54+08:00
# @require     :  Python 3.11.6
# @function    :
"""

import gc
import os
import time
from typing import Union
import argparse
import subprocess
from datetime import datetime
from utils.constants import PROJECT_ROOT_DIRECTORY, PYTEST_LOGS_DIRECTORY
from utils.device import get_device_list

FOREGROUND_RED = "\033[31m"
FOREGROUND_GREEN = "\033[32m"
ENDCOLOR = "\033[0m"


def run_pytest(
    serial_number: Union[str, None] = None,
    timestamp: Union[str, None] = None,
    markers: Union[str, None] = None,
    pull: bool = False,
    vertical: bool = False,
):
    """
    Function :
    """
    # run pytest with serial_number one by one.
    # sanity check
    assert serial_number is not None
    assert timestamp is not None
    assert markers is not None
    print(f"# {FOREGROUND_GREEN} serial_number = {serial_number} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} timestamp     = {timestamp} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} markers       = {markers} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} pull          = {pull} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} vertical      = {vertical} {ENDCOLOR}", flush=True)

    ################################################################
    os.makedirs(PYTEST_LOGS_DIRECTORY, exist_ok=True)
    print(f"# {PYTEST_LOGS_DIRECTORY}", flush=True)
    ################################################################

    pytest_log_stemname = f"pytest_{serial_number}_{timestamp}"
    ################################################################
    logger_directory = os.path.join(PYTEST_LOGS_DIRECTORY, pytest_log_stemname)
    os.makedirs(logger_directory, exist_ok=True)
    print(f"# {logger_directory}", flush=True)
    ################################################################

    pytest_console_log_filename = os.path.join(logger_directory, f"{pytest_log_stemname}.log")
    print(f"# {pytest_console_log_filename}", flush=True)
    pytest_main_filename = os.path.join(PROJECT_ROOT_DIRECTORY, "main.py")
    print(f"# {pytest_main_filename}", flush=True)
    with open(pytest_console_log_filename, mode="w", encoding="utf-8") as file:
        command = ["python3", pytest_main_filename, "-s", serial_number, "-t", timestamp, "-m", markers]
        if pull:
            command.append("--pull")
        if vertical:
            command.append("--vertical")
        with subprocess.Popen(" ".join(command), stdout=file, stderr=file, shell=True) as process:
            print(f"# main.py pid = {process.pid}", flush=True)


def measurer(func):
    """
    Function : measurer
    """

    def wrapper(*args, **kwargs):
        """
        Function : wrapper
        """
        start = time.time()
        func(*args, **kwargs)
        print(f"# elapsed time:{time.time() - start}")

    return wrapper


# @measurer
def main():
    """
    Function :
    """
    # sanity check
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--serial_number", action="store", default=None, dest="serial_number", help="serial_number")
    parser.add_argument("-m", "--markers", action="append", default=None, dest="markers", help="pytest markers")
    parser.add_argument("--pull", action="store_true", default=False, dest="pull", help="pull camera files")
    parser.add_argument("--vertical", action="store_true", default=False, dest="vertical", help=" vertical test mode")
    given = parser.parse_args()
    if given.serial_number is None or given.serial_number == "":
        parser.print_help()
        return
    if given.markers is None or given.markers == "":
        parser.print_help()
        return
    if given.serial_number not in get_device_list():
        return
    for each in given.markers:
        # [enter][manually trigger garbage collection]
        print(f"collected={gc.collect()}")
        # [leave][manually trigger garbage collection]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # [enter]only one marker to reduce memory consumption
        run_pytest(given.serial_number, timestamp, each, given.pull, given.vertical)
        time.sleep(6)
        # [leave]only one marker to reduce memory consumption
        # [enter][manually trigger garbage collection]
        print(f"collected={gc.collect()}")
        # [leave][manually trigger garbage collection]


if __name__ == "__main__":
    main()
