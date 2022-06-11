import os
import platform
import sys

def find_production_file(directory, file_name, ext, excl_dirs=None):
    exclude_dirs = ['_OLD', '_TEMP', '_gsdata_'] 
    if excl_dirs:
        exclude_dirs = excl_dirs
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file == (file_name + ext):
                return os.path.normpath(os.path.join(root, file))

def find_folder_path(directory, dir_name, excl_dirs=None):
    exclude_dirs = ['_OLD', '_TEMP', '_gsdata_'] 
    if excl_dirs:
        exclude_dirs = excl_dirs
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        if root.endswith(dir_name):
            return os.path.normpath(root)
            
def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return dir_path

def get_root_dir():
    return os.path.dirname(os.path.abspath(os.curdir))

def get_platform_info():
    os_name = platform.system()
    current_version = platform.release()
    system_info = platform.platform()
    python_version = sys.version
    return f'{os_name}_{current_version}_{system_info}_{python_version}'

def set_sep(str):
    new_str = str.replace('\\', '/')
    return new_str
