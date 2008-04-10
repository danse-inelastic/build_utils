"""
handle paths for mpich2 package
"""

name = 'mpich2'
description = 'Argonne MPI implementation'

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


fromEnvVars = PathsFinder( name, description, hints = "mpich2" )


from FromExecutable import PathsFinder
fromExe = PathsFinder( name, description, hints = {"executable": "mpirun.py"} )

toolset  = [fromEnvVars,
            fromExe,]


from search import search
paths = search(toolset)

