#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def copy_all( src, target, **opts ):
    "copy everything under src to target"
    from distutils.dir_util import copy_tree
    copy_tree( src, target, **opts )
    return



fmtstr = """
root=%s
deps=$root/deps

export PYRE_DIR=$root
export PATH=$root/bin:$deps/bin:$PATH
export LD_LIBRARY_PATH=$root/lib:$deps/lib:$LD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$root/lib:$deps/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=$root/modules:$deps/python:$PYTHONPATH
"""

def build_envs_sh( target ):
    "build envs.sh on target's bin directory"
    import os
    target = os.path.abspath( target )
    s = fmtstr % target
    f = os.path.join( target, 'bin', 'envs.sh' )
    open(f, 'w').write(s )
    return
    

# version
__id__ = "$Id$"

# End of file 
