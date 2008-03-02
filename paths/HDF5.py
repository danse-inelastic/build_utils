"""
handle paths for HDF5 package
"""

name = 'hdf5'
description = 'NCSA Hierarchiacal Data Format'

from FromEnvVariables import PathsFinder as _EnvPFBase

class PathsFinder(_EnvPFBase):
    import os
    if os.name == "nt":
        scheme = {'root': '.',
                  'c headers': 'include',
                  'c libraries': 'dll',
                  'python modules': 'python'}
        pass
    pass # end of PathsFinder


fromEnvVars = PathsFinder( name, description, hints = "HDF5" )


from FromExecutable import PathsFinder
fromExe = PathsFinder( name, description, hints = {"executable": "h5cc"} )

toolset  = [fromEnvVars,
            fromExe,]


from search import search
paths = search(toolset)

