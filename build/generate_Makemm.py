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

# make-Makemm.py <directory> <projectname>

# this module requires that the path to the root of the releaser to be included
# in PYTHONPATH

def main():
    import sys
    project = sys.argv[1]
    path = sys.argv[0]
    render(path, project)
    return


def render(path, project):
    import os
    
    d = { 'project': project }
    
    import packages
    table = packages.packageInfoTable

    dirs = []
    for name, info in table.iteritems():
        dirs.append( info['path'] )
        continue

    dirs = ''.join( ['\t%s \\\n' % dir for dir in dirs] )
    d['directories'] = dirs
    
    path = os.path.abspath( __file__ )
    path = os.path.dirname( path )

    fmtstr = open( os.path.join( path, 'Make.mm.template' ) ).read()
    s = fmtstr % d

    open( os.path.join( path, 'Make.mm' ), 'w' ).write( s )
    return



if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 


