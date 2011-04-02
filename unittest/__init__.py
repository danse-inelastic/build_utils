# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

def runAll(path):
    """run all unit tests in the given path
    
    Some parameters are loaded from <path>/config.py
    """
    import os
    config = os.path.join(path, 'config.py')
    if os.path.exists(config):
        opts = _loadConfiguration(config)
    else:
        opts = {}
    from run_tests import runtests
    return runtests(path, **opts)


from run_tests import printResult


def _loadConfiguration(config):
    from config_utils import load
    return load(config)


# version
__id__ = "$Id$"

# End of file 
