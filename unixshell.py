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



def execute( cmd, dry_run = False ):
    'execute a shell command'
    print 'executing %r... ' % cmd
    if dry_run: return
    if os.system(cmd) : raise RuntimeError , "%r failed" % cmd
    return


import os


# version
__id__ = "$Id$"

# End of file 
