"""
handle paths for boost python package
"""

name = 'boostpython'
description = 'boost python'

from FromEnvVariables import PathsFinder
fromEnvVars = PathsFinder( name, description, hints = "BOOSTPYTHON" )


toolset  = [fromEnvVars,
            ]


from search import search
paths = search(toolset)


#make sure headers are installed
from InstallationNotFound import InstallationNotFound

# header directory
include = paths.includes[0]
# make sure we can find boost/python.hpp
import os
python_hpp = os.path.join( include, 'boost', 'python.hpp' )
if not os.path.exists( python_hpp ):
    raise InstallationNotFound, name
