print("imported from import_from_same_dir")

# we can do this import even though pycharm complains
import sys
sys.path.append(".")


# if the file is imported from outside of this package, it is good to do this just in case
import sys, os
#SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
#sys.path.append(SCRIPT_DIR)

# assuming file_to_be_imported is in the same directory
from file_to_be_imported import Demo
from file_to_be_imported import func


Demo()
func()