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


def build_release(
    releaser_root,
    tmp = None,
    export_root = None, src_root = None,
    build_root = None,
    ):

    '''build a release

    releaser_root: root directory of releaser
    tmp: tmporary path. usually $releaser_root/tmp
    export_root: root where binaries and python modules to be exported. usually $releaser_root/EXPORT
    src_root: path to the sources. usually $releaser_root/sr
    '''
    
    if tmp is None: tmp = os.path.join(  releaser_root, 'tmp' )
    if export_root is None: export_root = os.path.join( releaser_root, 'EXPORT' )
    if src_root is None: src_root = os.path.join( releaser_root, 'src' )

    #get release info
    import release
    
    if release.identifier == "":
        print "$0 <name-of-release>"
        sys.exit(2)
        raise 

    from packages import packageInfoTable
    config_dir = os.path.join( src_root, packageInfoTable['config']['path'] )

    if build_root is None: build_root = os.path.join(
        tmp, 'build' )
    
    import build
    build.run( release.name, src_root, export_root, build_root, config_dir)

    clean_up( export_root )
    return


def clean_up( export_root ):
    patterns = [ '.svn', 'CVS', '.pyc' ]
    for pattern in patterns: prune( export_root, pattern )
    return


def prune( path, pattern ):
    cmd = r'find "%s" -name "%s" -exec rm -rf {} \;' % (
        path, pattern )
    print "running %r..." % cmd
    os.system( cmd )
    return


import sys, os



# version
__id__ = "$Id$"

# End of file 
