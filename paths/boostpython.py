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

