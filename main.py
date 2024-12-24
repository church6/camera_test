#!/usr/bin/python3
"""
# @filename    :  main.py
# @author      :  Copyright (C) Church.ZHONG
# @date        :  2024-03-27T09:34:57+08:00
"""

import gc
import os
import time
from typing import Union
import argparse
from datetime import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
import multiprocessing
import ctypes
import pytest
from utils.enums import EnumDeviceChargeState
from utils.features import get_variant_feature_by_product
from utils.constants import PROJECT_ROOT_DIRECTORY
from utils.run import run
from utils.ulog import Ulog
from utils.android import root_device
from utils.device import get_device_list, device_is_online
from utils.uenv import Uenv
from utils.errors import catch_error


def get_logger(
    product_name: Union[str, None] = None,
    serial_number: Union[str, None] = None,
    timestamp: Union[str, None] = None,
    directory: Union[str, None] = None,
    name: Union[str, None] = None,
):
    """
    Function :
    """
    # sanity check
    assert product_name is not None
    assert serial_number is not None
    assert timestamp is not None
    assert directory is not None
    assert directory != ""
    assert name is not None
    assert name != ""
    filename = os.path.join(directory, f"{name}.log")
    logger = logging.getLogger(name=f"{product_name}_{serial_number}_{timestamp}_{name}")
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(filename=filename, when="M", interval=30, backupCount=9, encoding="utf-8")
    handler.suffix = "%Y%m%d_%H%M%S"
    formatter = logging.Formatter(fmt="%(message)s", datefmt=None)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def write_sysinfo(writer=None, ulog=None):
    """
    Function :
    """
    # sanity check
    assert writer is not None
    assert ulog is not None
    serial_number = ulog.get_serial_number()
    # [enter][battery]log timestamp comes first
    writer("%s battery_capacity=%s", datetime.now(), ulog.get_udev().get_battery_capacity())
    # [leave][battery]log timestamp comes first
    get = run(f'adb -s {serial_number} shell "dumpsys cpuinfo 2>/dev/null"')
    if get.status:
        writer(get.capture)


def sysinfo_worker(event_pytest3_finished=None, ulog=None, namespace_testnode_filename=None, namespace_testnode_funcname=None):
    """
    Function :
    """
    # run worker with serial_number one by one.
    # sanity check
    assert event_pytest3_finished is not None
    assert ulog is not None
    assert namespace_testnode_filename is not None
    assert namespace_testnode_funcname is not None
    log = ulog.get_camera_logger()
    product_name = ulog.get_product_name()
    serial_number = ulog.get_serial_number()
    timestamp = ulog.get_timestamp()
    log.info("[enter]%s,%s,%s (pid=%d)", product_name, serial_number, timestamp, os.getpid())

    sysinfo_directory = ulog.get_sysinfo_directory()
    writer = get_logger(
        product_name=product_name, serial_number=serial_number, timestamp=timestamp, directory=sysinfo_directory, name="sysinfo"
    ).info
    while True:
        if event_pytest3_finished.is_set():
            log.warning("event_pytest3_finished is set")
            break
        if not device_is_online(serial_number):
            log.warning("offline:%s", serial_number)
            break
        # [enter]dut is sleep and in charging
        if ulog.get_shared_number1() == EnumDeviceChargeState.TYPE_DEVICE_IS_YES_IN_CHARGING:
            continue
        # [leave]dut is sleep and in charging

        write_sysinfo(writer=writer, ulog=ulog)
        time.sleep(2)
    # Process finished after received notification
    log.info("[leave]%s,%s,%s", product_name, serial_number, timestamp)


def write_appinfo(writer=None, ulog=None):
    """
    Function :
    """
    # sanity check
    assert writer is not None
    assert ulog is not None
    serial_number = ulog.get_serial_number()
    # [enter][battery]log timestamp comes first
    writer("%s battery_capacity=%s", datetime.now(), ulog.get_udev().get_battery_capacity())
    # [leave][battery]log timestamp comes first

    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME
    camera_provider_process_name = get_variant_feature_by_product(ulog=ulog).QTI_CAMERA_PROVIDER_PROCESS_NAME
    pids = {camera_provider_process_name: 0, camera_package_name: 0}
    for process in pids:
        # [enter][pid]log timestamp comes first
        get = run(f"adb -s {serial_number} shell pgrep -o -f {process}")
        if not get.status:
            continue
        pid = int(get.capture)
        pids[process] = pid
        writer("%s %s=%s", datetime.now(), process, pid)
        # [leave][pid]log timestamp comes first

        # [enter]/proc/<pid>/status
        # get = run(f'adb -s {serial_number} shell "cat /proc/{pid}/status 2>/dev/null"')
        # if get.status:
        #     writer(get.capture)
        # [leave]/proc/<pid>/status

    camera_provider_pid = pids[camera_provider_process_name]
    # [enter][debuggerd]
    # get = run(f'adb -s {serial_number} shell "debuggerd -b {camera_provider_pid} 2>/dev/null"')
    # if get.status:
    #     writer(get.capture)
    #  [leave][debuggerd]

    # [enter]meminfo
    get = run(f"adb -s {serial_number} shell dumpsys meminfo {camera_package_name}")
    if get.status:
        writer(get.capture)
    get = run(f"adb -s {serial_number} shell procrank -d {camera_provider_pid} 2>/dev/null")
    if get.status:
        writer(get.capture)
    # [leave]meminfo
    return camera_provider_pid


def appinfo_worker(event_pytest3_finished=None, ulog=None, namespace_testnode_filename=None, namespace_testnode_funcname=None):
    """
    Function :
    """
    # run worker with serial_number one by one.
    # sanity check
    assert event_pytest3_finished is not None
    assert ulog is not None
    assert namespace_testnode_filename is not None
    assert namespace_testnode_funcname is not None
    log = ulog.get_camera_logger()
    product_name = ulog.get_product_name()
    serial_number = ulog.get_serial_number()
    timestamp = ulog.get_timestamp()
    log.info("[enter]%s,%s,%s (pid=%d)", product_name, serial_number, timestamp, os.getpid())

    exception_timestamp = ""
    camera_provider_process_name = get_variant_feature_by_product(ulog=ulog).QTI_CAMERA_PROVIDER_PROCESS_NAME
    get = run(f"adb -s {serial_number} shell pgrep -o -f {camera_provider_process_name}")
    assert get.status
    camera_provider_pid = int(get.capture)
    appinfo_directory = ulog.get_appinfo_directory()
    writer = get_logger(
        product_name=product_name, serial_number=serial_number, timestamp=timestamp, directory=appinfo_directory, name="appinfo"
    ).info
    while True:
        if event_pytest3_finished.is_set():
            log.warning("event_pytest3_finished is set")
            break
        if not device_is_online(serial_number):
            log.warning("offline:%s", serial_number)
            break
        # [enter]dut is sleep and in charging
        if ulog.get_shared_number1() == EnumDeviceChargeState.TYPE_DEVICE_IS_YES_IN_CHARGING:
            continue
        # [leave]dut is sleep and in charging

        pid = write_appinfo(writer=writer, ulog=ulog)
        # [enter]detect whether provider is crashed
        if camera_provider_pid != pid:
            camera_provider_pid = pid
            exception_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ulog.set_testnode(namespace_testnode_filename.shared_str, namespace_testnode_funcname.shared_str)
            time.sleep(2)
            catch_error(timestamp=exception_timestamp, ulog=ulog, witness="appinfo", forced=True)
            continue
        # [leave]detect whether provider is crashed

        time.sleep(2)
    # Process finished after received notification
    log.info("[leave]%s,%s,%s", product_name, serial_number, timestamp)


def pytest3_worker(event_pytest3_finished=None, ulog=None, namespace_testnode_filename=None, namespace_testnode_funcname=None):
    """
    Function :
    """
    # run worker with serial_number one by one.
    # sanity check
    assert event_pytest3_finished is not None
    assert ulog is not None
    assert namespace_testnode_filename is not None
    assert namespace_testnode_funcname is not None
    log = ulog.get_camera_logger()
    product_name = ulog.get_product_name()
    serial_number = ulog.get_serial_number()
    timestamp = ulog.get_timestamp()
    log.info("[enter]%s,%s,%s (pid=%d)", product_name, serial_number, timestamp, os.getpid())
    device = ulog.get_device()
    camera_package_name = get_variant_feature_by_product(ulog=ulog).HMD_CAMERA_PACKAGE_NAME
    app_info = device.app_info(package_name=camera_package_name)
    log.info("app_info:%s", str(app_info))
    log.info("app_name:%s", camera_package_name)
    env = Uenv(product_name, serial_number, timestamp)
    env.set_env_by_key(key="camera_app_versionName", value=app_info["versionName"])
    env.set_env_by_key(key="camera_app_versionCode", value=app_info["versionCode"])

    # report_html = ulog.get_report_html_filename()
    array = env.get_env_by_key(key="markers").split(",")
    command = [
        # "-v",
        "-s",
        "-c",
        os.path.join(PROJECT_ROOT_DIRECTORY, "pytest.ini"),
        f"--junit-xml={ulog.get_junit_filename()}",
        f"--alluredir={ulog.get_allure_directory()}",
        f"--product_name={product_name}",
        f"--serial_number={serial_number}",
        f"--timestamp={timestamp}",
        "--cache-clear",
        "-m",
        " or ".join(array),
    ]
    log.info("command=%s", " ".join(command))
    os.chdir(PROJECT_ROOT_DIRECTORY)
    pytest.main(command)
    log.info("[leave]%s,%s,%s", product_name, serial_number, timestamp)
    # [enter]Process finished then sent notification
    event_pytest3_finished.set()
    # [leave]Process finished then sent notification


def works(env: Union[Uenv, None] = None):
    """
    Function :
    """
    # run pytest with serial_number one by one.
    # sanity check
    assert env is not None
    product_name = env.get_product_name()
    serial_number = env.get_serial_number()
    timestamp = env.get_timestamp()
    with multiprocessing.Manager() as manager:
        namespace_testnode_filename = manager.Namespace()
        namespace_testnode_filename.shared_str = str(__file__)
        namespace_testnode_funcname = manager.Namespace()
        namespace_testnode_funcname.shared_str = str("__main__")
        processes = []
        # [enter][ulog][multiprocessing]
        root_device(serial_number)
        singleton = Ulog(product_name, serial_number, timestamp)
        singleton.init_testnode(namespace_testnode_filename, namespace_testnode_funcname)
        event_pytest3_finished = multiprocessing.Event()
        shared_value1 = multiprocessing.Value(ctypes.c_uint, 0)
        singleton.set_shared_value1(shared_value1)
        arguments = (event_pytest3_finished, singleton, namespace_testnode_filename, namespace_testnode_funcname)
        # process = multiprocessing.Process(target=sysinfo_worker, args=arguments)
        # processes.append(process)
        process = multiprocessing.Process(target=appinfo_worker, args=arguments)
        processes.append(process)
        process = multiprocessing.Process(target=pytest3_worker, args=arguments)
        processes.append(process)
        # [leave][ulog][multiprocessing]

        print(f"[enter]All {len(processes)} processes have started.")
        # [enter][manually trigger garbage collection]
        singleton.get_camera_logger().info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        for process in processes:
            process.start()

        for process in processes:
            process.join()
        # [enter][manually trigger garbage collection]
        singleton.get_camera_logger().info("collected=%s", gc.collect())
        # [leave][manually trigger garbage collection]
        print(f"[leave]All {len(processes)} processes have finished.")


def main():
    """
    Function :
    """
    # sanity check
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--serial_number", action="store", default=None, dest="serial_number", help="serial_number")
    parser.add_argument("-t", "--timestamp", action="store", default=None, dest="timestamp", help="pytest timestamp")
    parser.add_argument("-m", "--markers", action="store", default=None, dest="markers", help="pytest markers")
    parser.add_argument("--pull", action="store_true", default=False, dest="pull", help="pull camera files")
    parser.add_argument("--vertical", action="store_true", default=False, dest="vertical", help="vertical test mode")
    given = parser.parse_args()
    if given.serial_number is None or given.serial_number == "":
        parser.print_help()
        return
    if given.timestamp is None or given.timestamp == "":
        parser.print_help()
        return
    if given.markers is None or given.markers == "":
        parser.print_help()
        return
    if not device_is_online(given.serial_number):
        print(f"offline:{given.serial_number}")
        return

    # [enter][manually trigger garbage collection]
    device_count = len(get_device_list())
    (threshold0, threshold1, threshold2) = gc.get_threshold()
    print(f"threshold0, threshold1, threshold2 = {threshold0}, {threshold1}, {threshold2}")
    threshold0 = threshold0 // (device_count + 1)
    gc.set_threshold(threshold0, threshold1, threshold2)
    print(f"threshold0, threshold1, threshold2 = {threshold0}, {threshold1}, {threshold2}")
    # [leave][manually trigger garbage collection]

    get = run(f"adb -s {given.serial_number} shell getprop ro.product.board")
    assert get.status
    product_name, serial_number, timestamp = get.capture.lower(), given.serial_number, given.timestamp
    array = given.markers.split(",")
    array.insert(0, "warmup")
    env = Uenv(product_name, serial_number, timestamp)
    env.set_env_by_key(key="markers", value=",".join(array))
    env.set_env_by_key(key="project_root_directory", value=PROJECT_ROOT_DIRECTORY)
    env.set_env_by_key(key="config_pull_dut_dcim_file", value=given.pull)
    env.set_env_by_key(key="config_vertical_test_mode", value=given.vertical)
    works(env)


if __name__ == "__main__":
    main()
