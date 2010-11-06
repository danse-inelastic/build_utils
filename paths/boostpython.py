"""
handle paths for boost python package
"""

name = 'boostpython'
description = 'boost python'



def validate(paths):
    import os
    from PathsFinder import assertExists
    assertExists('boost/python.hpp', paths.includes)
    assertExists('libboost_python.so*', paths.clibs)
    return


from FromDefaultLocations import PathsFinder
fromDefaultLoc = PathsFinder(name, description, validator=validate)


from FromEnvVariables import PathsFinder
fromEnvVars = PathsFinder(
    name, description,
    hints = "BOOSTPYTHON" ,
    validator = validate)


toolset  = [fromDefaultLoc, fromEnvVars]


from search import search
paths = search(toolset)


