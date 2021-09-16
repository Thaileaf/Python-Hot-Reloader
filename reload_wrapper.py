import importlib
import sys
import time
import keyboard
import os

# List of modules to check source code change for
MODULES = ['test.py']

# How long in seconds to poll for changes
POLL_TIME = 1

# Working directory
WORK_DIR = r"C:\Users\letha\PycharmProjects\NewSchool"


def run() -> None:
    """
    Main run loop

    :return: null
    """
    print("\033[1;31;40m Reload Loop Started \033[0m")
    import_mod(MODULES)
    while not keyboard.is_pressed('esc'):
        time.sleep(1)
        reload()


def reload() -> None:
    """
    Loads/Reloads the module in global variable modules

    :return:
    """
    for module in MODULES:
        try:
            # Checks if the code has been modified in the past 2 seconds and reloads if so
            if time.time() - os.path.getmtime(os.path.join(WORK_DIR, module)) < 1:
                # Shows user that module is reloaded
                print("\033[1;33;45m" + ("-" * 25) + "Reloaded Module" + ("-" * 25) + "\033[0m")
                importlib.reload(sys.modules.get(module.strip(".py"), 'sys'))


        except TypeError:
            import_mod([module])

        except Exception as e:
            print(type(e).__name__ + ": ", e)

def compare(path1: str, path2: str) -> bool:
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

def import_mod(modules: list) -> None:
    """
    This is the initial import of each module in the list of modules
    :param modules: str - List of modules to import
    :return:
    """
    for module in modules:
        try:
            importlib.import_module(module.strip(".py"), 'NewSchool')

        except Exception as e:
            print(type(e).__name__ + ": ", e)