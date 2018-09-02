# we can do this import even though pycharm complains

# 1 - same folder
import module_to_be_imported_same
module_to_be_imported_same.Demo()

# 2 - folder below
from package3 import module_to_be_imported_sub
module_to_be_imported_sub.Demo()

# 3 - folder above

import sys
sys.path.append('..')
import module_to_be_imported_parent
module_to_be_imported_parent.Demo()

'''
# Note that this would not work

from demo import module_to_be_imported_parent

'''

# 4 - cross folder
import sys
sys.path.append('../package2')
import module_to_be_imported_cross
module_to_be_imported_cross.Demo()

'''
# Note that this would not work as well

from demo.package2 import module_to_be_imported_cross

'''
