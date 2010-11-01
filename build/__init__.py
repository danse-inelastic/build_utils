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


def get_release():
    #get release info
    import release
    
    if release.identifier == "":
        raise RuntimeError, "release identifier not specified"

    return release


def build_release(releaser_root):
    'build a release'
    release = get_release()
    return _build( release, build_dirs( releaser_root ) )


def build_docs(releaser_root):
    'build a release'
    release = get_release()
    return _build( release, build_dirs( releaser_root ), args = ['docs'] )


def build_dirs( root, tmp = None, export = None, src = None, build = None ):
    '''create a data object to hold directories related to a build
    
    root: root directory of releaser
    tmp: tmporary path. usually $root/tmp
    export: root where binaries and python modules to be exported. usually $root/EXPORT
    src: path to the sources. usually $root/src
    '''
    if export is None: export = os.path.join( root, 'EXPORT' )
    if src is None: src = os.path.join( root, 'src' )
    if tmp is None: tmp = os.path.join(  root, 'tmp' )
    if build is None: build = os.path.join(tmp, 'build' )

    from BuildDirs import BuildDirs
    return BuildDirs( root, src, export, build, tmp)


def _build(release, builddirs, args = []):
    '''build

    builddirs: directories of the build (instance of BuildDirs)
    '''
    
    import packages
    packageInfoTable = getattr(packages, 'packageInfoTable', None)
    
    if packageInfoTable:
        # old "packages"
        config_dir = packageInfoTable['config']['path']
    else:
        # new oo "packages"
        from packages import config
        config_dir = config.name
    config_dir = os.path.join( builddirs.src, config_dir)

    import build
    succeeded = False
    while not succeeded:
        try:
            build.run(
                release.name, builddirs.src, builddirs.export,
                builddirs.build, config_dir,
                arguments = args)
            succeeded = True
        except build.DependencyMissing, err:

            depname = err.packagename
            depid = err.packageid

            print '*** Dependency %s is missing ***' % depname

            # error message
            if err.errormessage:
                msg = err.errormessage
                
            from ..misc._formatstr import indent
            msg = indent(msg, '| ')
            print '* Error:\n%s\n' % msg

            # suggestion
            if err.suggestion:
                print '* Suggestion:\n%s\n' % err.suggestion
                
            print '* This builder could try to install it locally.'
            
            if raw_input(" * Install dependency '%s'? (yes/no) " % depname) != 'yes': 
                print "\nAbort\n"
                return

            print "Trying to install dependency '%s' ..." % depname

            # is installer specified?
            from deps import installers
            installer = installers.get( depid )

            # use default installer if possible
            if installer is None:
                installer = get_installer( depid )

            # install
            installer()
                
            #after installation, we want to make sure installation
            #is successful. 
            checkInstallation( depid )
            pass
        continue

    clean_up( builddirs.export )
    return


def checkInstallation( dep ):
    from utils.paths import get, InstallationNotFound
    try: get(dep)
    except InstallationNotFound:
        lines = (
            'Dependency %r was not installed successfully.' % dep,
            'Sometimes this can be solved by rerun the',
            'installation or build script',
            )
        msg =  ' '.join(lines)
        print msg
        import sys
        sys.exit(1)
        raise
    return


def get_installer( dep ):
    from utils.installers import guess
    return guess( dep )


def clean_up( export_root, patterns = [ '.svn', 'CVS', '.pyc' ] ):
    for pattern in patterns: prune( export_root, pattern )
    return


def prune( path, pattern ):
    cmd = r'find "%s" -name "%s" -exec rm -rf {} \;' % (
        path, pattern )
    print "running %r..." % cmd
    os.system( cmd )
    return


import sys, os
import utils.installers



# version
__id__ = "$Id$"

# End of file 
