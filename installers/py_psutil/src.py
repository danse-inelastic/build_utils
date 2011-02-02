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


name = 'psutil'

def get( version = None, **kwds ):
    cmd = 'easy_install --prefix="%s" psutil' % (install_path,)
    def _():
        return execute(cmd)
    return _
    

from utils.installers import install_path, execute



# version
__id__ = "$Id$"

# End of file 
