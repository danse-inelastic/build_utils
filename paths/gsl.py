"""
handle paths for GSL package
"""

from InstallationNotFound import InstallationNotFound

name = 'gsl'
description = 'GNU scientific library'

# validator 
# search all include dirs to find gsl/gsl_version.h
def validator(paths):
    import os
    found = False
    for directory in paths.includes:
        candidate = os.path.join(directory, 'gsl', 'gsl_version.h')
        print "* Looking for %s" % candidate
        if os.path.exists(candidate): found=True; break
        print "... not found"
        continue
    if not found: 
        raise RuntimeError, "Cannot find gsl/gsl_version.h in candidate %s" % paths
    return



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
fromEnvVars = PathsFinder( name, description, hints = "GSL", validator=validator) 


from FromExecutable import PathsFinder
fromExe = PathsFinder( name, description, hints = {"executable": "gsl-config"}, validator=validator)


toolset  = [fromEnvVars, fromExe]


def find():
    from search import search
    paths = search(toolset)
    return paths
