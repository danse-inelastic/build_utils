"""
handle paths for pylons
"""

name = 'pylons'
description = 'a python lightweight web framework'


from InstallationNotFound import InstallationNotFound

try:
    pylons = __import__('pylons', {}, {}, [] )
except ImportError:
    raise InstallationNotFound, "pylons"


from Paths import Paths

paths = Paths( name, description = description )

