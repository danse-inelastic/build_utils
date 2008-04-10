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

def render( paths ):
    root = paths.root
    lines = [
        "export MPI_DIR='%s'" % root,
        "export MPI_INCDIR='%s'" % paths.includes[0],
        "export MPI_LIBDIR='%s'" % paths.clibs[0],
        #"export MPI_INCLUDES='%s'" % ':'.join(paths.includes),
        #"export MPI_LIBS='%s'" % ':'.join(paths.clibs),
        ]
    return lines
        

# version
__id__ = "$Id$"

# End of file 
