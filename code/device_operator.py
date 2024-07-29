"""
interact with the device
"""
import os
import time
import page_reproducer
from json_extractor import _AndroidDevice

device = None
d = None
device_name = None


def setup(device_number):
    global device_name
    device_name = device_number


def activate_device():
    global device
    global d
    global device_name
    device = _AndroidDevice(device_name)
    d = device.d


def start_app(launch_activity):
    global device_name
    start_app_cmd = "adb -s " + device_name + " shell am start -n " + launch_activity
    os.system(start_app_cmd)
    time.sleep(3)
    page_reproducer.collect(f'os.system("{start_app_cmd}")')


def stop_app(package_name):
    global device_name
    stop_app_cmd = "adb -s " + device_name + " shell am force-stop " + package_name
    os.system(stop_app_cmd)
    time.sleep(3)
    page_reproducer.collect(f'os.system("{stop_app_cmd}")')


def exec_code(code):
    exec(code)
    time.sleep(3)
