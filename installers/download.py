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


def download_cmd( link ):
    if link.startswith( 'http:' ):
        return [ 'wget %s' % link ]
    elif link.startswith( 'svn:' ):
        return download_using_svn( link )
    else:
        raise NotImplementedError

def download_using_svn( link ):
    import os
    path, filename = os.path.split( link )
    dirname = os.path.split( path )[-1]
    cmds = [
        # check out directory
        'svn co -N %s' % path,
        # cd into the directory and get file
        'cd %s' % dirname,
        'svn up %s' % filename,
        # mv file up
        'mv %s ..' % filename,
        # remove directory
        'cd ..',
        'rm -rf %s' % dirname,
        ]
    return cmds


# version
__id__ = "$Id$"

# End of file 
