"""
handle paths for mmtk
"""

name = 'mmtk'
description = 'mmtk'


from InstallationNotFound import InstallationNotFound

try:
    import MMTK
except ImportError, err:
    import traceback
    print traceback.format_exc()
    raise InstallationNotFound, name

import os


from Paths import Paths

paths = Paths(name, description = description)

