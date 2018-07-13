print("imported from import_from_parent_dir")


import os, sys

# import from a parent directory

# add the parent directory to path
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# do the actual import
import import_from_sub_dir

