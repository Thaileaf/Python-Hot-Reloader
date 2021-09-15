import importlib
import sys
import time
import keyboard
import os

# List of modules to check source code change for
MODULES = ['test.py']

# How long in seconds to poll for changes
POLL_TIME = 1

# Working director
WORK_DIR = r"C:\Users\letha\PycharmProjects\NewSchool"


def run():
    """
    Main run loop

    :return: null
    """
    while not keyboard.is_pressed('esc'):
        print('test')
        time.sleep(1)
        reload()


def reload():
    """
    Loads/Reloads the module in global variable modules

    :return: null
    """
    for module in MODULES:
        # Checks if the code has been modified in the past 2 seconds and reloads if so
        if time.time() - os.path.getmtime(os.path.join(WORK_DIR, module)) < 2:
            importlib.reload(sys.modules.get(module, 'sys'))
            print('reloaded')
        print('file unchanged')

def compare(path1, path2):
    """
    Compares two files
    :param path1: str
    :param path2: str
    :return: bool
    """
    with open(path1) as file1:
        with open(path2) as file2:
            if file1.read() == file2.read():
                return True
            else:
                return False

def import_mod(modules):
    """

    :param modules: str - List of modules to import
    :return:
    """

    return
