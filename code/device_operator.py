"""
interact with the device
"""
import os
import time
import page_reproducer
from json_extractor import simplify_json, _AndroidDevice, get_android_hierarchy

device = None
d = None
device_name = None
package_name = None


def setup(device_number, package):
    global device_name
    global package_name
    device_name = device_number
    package_name = package


def activate_device():
    global device
    global d
    global device_name
    global package_name
    device = _AndroidDevice(device_name, package_name)
    d = device.d
    d.implicitly_wait(5)


def start_app(launch_activity):
    # global device_name
    # start_app_cmd = "adb -s " + device_name + " shell am start -n " + launch_activity
    # os.system(start_app_cmd)
    # time.sleep(5)
    # page_reproducer.collect(f'os.system("{start_app_cmd}")')
    global d
    d.app_start(launch_activity)
    time.sleep(5)
    page_reproducer.collect(f'd.app_start("{launch_activity}", stop=True)')


def stop_app(package_name):
    # global device_name
    # stop_app_cmd = "adb -s " + device_name + " shell am force-stop " + package_name
    # os.system(stop_app_cmd)
    # time.sleep(5)
    # page_reproducer.collect(f'os.system("{stop_app_cmd}")')
    global d
    d.app_stop(package_name)
    time.sleep(3)
    d.press('home')
    page_reproducer.collect(f'd.app_stop("{package_name}")')
    page_reproducer.collect("d.press('home')")


def exec_code(code):
    exec(code)
    time.sleep(3)
    page_reproducer.collect(code)

