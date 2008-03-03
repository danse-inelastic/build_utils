"""
handle paths for numpy
"""

name = 'numpy'
description = 'numerical python'


from InstallationNotFound import InstallationNotFound

try:
    numpy = __import__('numpy', {}, {}, [] )
except ImportError:
    raise InstallationNotFound, "numpy"

import os
# numpy is strange because it installs its headers to python directory
include = os.path.join( os.path.split( numpy.__file__ )[0],
                        "core", "include" )

from Paths import Paths

paths = Paths( name, description = description, includes = [include] )

