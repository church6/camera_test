#!/usr/bin/python3
"""
# @filename    :  run.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-04-22T10:37:54+08:00
# @require     :  Python 3.11.6
# @function    :
"""

import os
import time
from typing import List, Union
import argparse
import configparser
import subprocess
from utils.constants import PROJECT_ROOT_DIRECTORY
from utils.device import get_device_list
from utils.run import run
from utils.features import DEFINED_NAMES_OF_PRODUCTS

FOREGROUND_RED = "\033[31m"
FOREGROUND_GREEN = "\033[32m"
ENDCOLOR = "\033[0m"


def get_pytest_markers():
    """
    Function :
    """
    # sanity check
    filename = os.path.join(PROJECT_ROOT_DIRECTORY, "pytest.ini")
    config = configparser.ConfigParser()
    config.read(filename, encoding="utf-8")
    markers = config.get("pytest", "markers")
    # print(markers)
    nvps = {}
    for each in markers.splitlines():
        if not each.strip():
            continue
        if ":" in each:
            splits = each.split(":")
            if len(splits) == 2:
                nvps[splits[1]] = splits[1]
        else:
            nvps[each] = each
    return nvps


def yes_or_no(question: Union[str, None] = None, loop: bool = False) -> bool:
    """
    Description :
    """
    # sanity check
    assert question is not None
    sisyphus = input(f"{FOREGROUND_RED}Ready? {question} (default is No)[y|n]{ENDCOLOR}")
    reply = str(sisyphus).lower().strip()
    length = len(reply)
    # print(f'# length = {length}')
    if length > 0:
        if reply[0] == "y":
            return True
        if reply[0] == "n":
            return False
    return loop and yes_or_no(question, loop)


def select_in_list(options=None, name: Union[str, None] = None, dic=None):
    """
    Function :
    """
    # sanity check
    assert options is not None
    assert name is not None
    option = None
    print(f"{FOREGROUND_GREEN}Please select the{ENDCOLOR} {FOREGROUND_RED}{name}{ENDCOLOR}:", flush=True)
    for index, option in enumerate(options):
        formated = option
        if dic is not None:
            formated = f"{option:<32s} -> {dic[option]}"
        print(f"{index + 1:<2d}) {formated}", flush=True)

    length = len(options)
    if length == 0:
        return option

    selected = False
    while not selected:
        raw = input("#? ")
        try:
            num = int(raw)
        except ValueError:
            print("please input a number!", flush=True)
            continue
        if 0 < num <= length:
            num = num - 1
            option = options[num]
            print(f'You have selected {FOREGROUND_RED}{name}{ENDCOLOR} = "{FOREGROUND_GREEN}{option}{ENDCOLOR}"', flush=True)
            selected = True
        else:
            pass
    return option


def run_pytest(
    serial_number: Union[str, None] = None, markers: Union[List[str], None] = None, pull: bool = False, vertical: bool = False
):
    """
    Function :
    """
    # pylint: disable=R1732
    # run pytest with serial_number one by one.
    # sanity check
    assert serial_number is not None
    assert markers is not None
    print(f"# {FOREGROUND_GREEN} serial_number = {serial_number} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} markers       = {markers} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} pull          = {pull} {ENDCOLOR}", flush=True)
    print(f"# {FOREGROUND_GREEN} vertical      = {vertical} {ENDCOLOR}", flush=True)

    ################################################################
    # pull = yes_or_no("测试过程是否将照片和视频保存到本地", loop=False)
    ################################################################

    wrapper_run_filename = os.path.join(PROJECT_ROOT_DIRECTORY, "wrapper_run.py")
    print(f"# {wrapper_run_filename}", flush=True)
    command = ["python3", wrapper_run_filename, "-s", serial_number]
    if pull:
        command.append("--pull")
    if vertical:
        command.append("--vertical")
    for marker in markers:
        command.append("-m")
        command.append(marker)
    print(" ".join(command))
    process = subprocess.Popen(" ".join(command), shell=True, stdout=subprocess.DEVNULL)
    print(f"# wrapper_run.py pid = {process.pid}", flush=True)
    time.sleep(3)
    process.kill()


COLLECTION_NVPS = get_pytest_markers()


def human_chose():
    """
    Function :
    """
    # sanity check
    selected = select_in_list(options=list(COLLECTION_NVPS.keys()), name="测试选项")
    assert selected is not None
    return COLLECTION_NVPS[selected]


def validate_product_name(serial_number: Union[str, None] = None) -> bool:
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    get = run(f"adb -s {serial_number} shell getprop ro.product.board")
    assert get.status
    product_name = get.capture.lower()
    assert product_name in DEFINED_NAMES_OF_PRODUCTS, f"product_name = {product_name}"
    print(f"# {FOREGROUND_GREEN} product_name  = {product_name} {ENDCOLOR}", flush=True)
    return True


def work(
    serial_number: Union[str, None] = None, markers: Union[List[int], None] = None, pull: bool = False, vertical: bool = False
):
    """
    Function :
    """
    # sanity check
    assert serial_number is not None
    assert markers is not None
    print(f"# serial_number = {serial_number}", flush=True)
    if not validate_product_name(serial_number):
        return
    selected: List[str] = []
    for each in markers:
        if each in COLLECTION_NVPS:
            selected.append(each)
    if len(markers) == 0:
        selected.append(human_chose())
    if selected:
        run_pytest(serial_number, selected, pull, vertical)


def main():
    """
    Function : main
    """
    # sanity check
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", default=False, dest="all", help="traverse all devices")
    parser.add_argument("-s", "--serial_number", action="store", default=None, dest="serial_number", help="serial_number")
    parser.add_argument("-e", "--enum", action="store_true", default=False, dest="enum", help="enum case")
    parser.add_argument("-m", "--markers", action="append", default=[], dest="markers", type=str, help="markers")
    parser.add_argument("--pull", action="store_true", default=False, dest="pull", help="pull camera files")
    parser.add_argument("--vertical", action="store_true", default=False, dest="vertical", help="vertical test mode")
    given = parser.parse_args()
    devices = get_device_list()

    if given.enum:
        for index, option in enumerate(COLLECTION_NVPS):
            print(f"{index + 1:<2d}) {option}", flush=True)
        return

    if given.all:
        for serial_number in devices:
            work(serial_number, given.markers, given.pull)
    else:
        serial_number = None
        if given.serial_number is not None and given.serial_number != "":
            serial_number = given.serial_number
        else:
            serial_number = select_in_list(devices, "device")
        if serial_number is None:
            print("serial_number is None")
            return
        if serial_number not in devices:
            print(f"{serial_number} is offline")
            return
        work(serial_number, given.markers, given.pull, given.vertical)


if __name__ == "__main__":
    main()
