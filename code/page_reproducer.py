"""
When the page rollback fails, the reproducer restores the page
"""
import time
import os

operation_collector = ""


def collect(operation):
    global operation_collector
    operation_collector += operation + '\n'


def reproduce():
    executed_codes = operation_collector.splitlines()
    for code in executed_codes:
        try:
            exec(code)
            time.sleep(3)
        except Exception as ex:
            pass

def clear():
    operation_collector = ""
