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


name = 'h5py'
server = "http://h5py.googlecode.com/files"
#http://code.google.com/p/h5py/downloads/detail?name=h5py-1.3.0.tar.gz

def get( version = None, **kwds ):
    if version is None: version = "1.3.0"
    cmd = 'python setup.py install --prefix=%s --install-lib=%s/python' % (
        install_path, install_path)
    def _():
        return install(
            name, version,
            server = server,
            install_commands = [cmd],
            **kwds )
    return _
    

from utils.installers.src import install, install_path


# version
__id__ = "$Id$"

# End of file 
