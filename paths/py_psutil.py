"""
handle paths for psutil
"""

name = 'py_psutil'
description = 'numerical python'


from InstallationNotFound import InstallationNotFound

try:
    import psutil
except ImportError, err:
    import traceback
    print traceback.format_exc()
    raise InstallationNotFound, name


from Paths import Paths

paths = Paths( name, description = description )

