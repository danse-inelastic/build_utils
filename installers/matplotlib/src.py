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


name = 'matplotlib'
server = 'http://superb-west.dl.sourceforge.net/sourceforge/matplotlib'

def get( version = None, **kwds ):
    if version is None: version = "0.90.1"
    cmds = [
        "python setup.py install --prefix=%s --install-lib=%s/python" % (
        install_path, install_path ),
        ]
    def _():
        install( name, version,
                 server = server, install_commands = cmds,
                 **kwds )
        return
    return _
    

from utils.installers.src import install, install_path



# version
__id__ = "$Id$"

# End of file 
