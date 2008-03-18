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

def get( package, type = 'src', version = None, platform = None, pyver = None,
         **kwds ):
    modulename = "%s.%s" % (package, type)
    try:
        exec "import %s as module" % modulename
    except ImportError:
        raise NotImplementedError, "installer for package %r, from %r" % (
            package, type)
    return module.get( version, platform = platform, pyver = pyver, **kwds )


import os
pwd = os.path.dirname( os.path.abspath( __file__ ) )
releaser_root = os.path.abspath( os.path.join(pwd, '..', '..' ) ) 
tarball_path = os.path.join(releaser_root, 'install-deps' )
if not os.path.exists( tarball_path ): os.makedirs( tarball_path )
if not os.path.isdir( tarball_path ): raise IOError, "%r is not a directory" % tarball_path

install_path = os.path.join( releaser_root, 'EXPORT', 'deps' )


#allow access to installed python package
import sys
sys.path = [os.path.join(install_path, 'python')] + sys.path

#bash only. bad hack...
os.environ['PATH'] = '%s:%s' % (
    os.path.join( install_path, 'bin' ), os.environ['PATH'] )
os.environ['LD_LIBRARY_PATH'] = '%s:%s' % (
    os.path.join( install_path, 'lib' ), os.environ.get('LD_LIBRARY_PATH') or '' )
os.environ['DYLD_LIBRARY_PATH'] = '%s:%s' % (
    os.path.join( install_path, 'lib' ), os.environ.get('DYLD_LIBRARY_PATH') or '' )



from utils.unixshell import execute


# version
__id__ = "$Id$"

# End of file 
