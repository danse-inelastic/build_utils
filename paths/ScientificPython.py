"""
handle paths for Scientific python
"""

name = 'ScientificPython'
description = 'Scientific python'


from InstallationNotFound import InstallationNotFound

try:
    import Scientific
except ImportError, err:
    import traceback
    print traceback.format_exc()
    raise InstallationNotFound, name

import os


from Paths import Paths

paths = Paths(name, description = description)

