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


def render_file( path, dependencies,
                 export_root, build_root, config_dir,
                 target = 'shared,opt' ):
    f = Factory( export_root, build_root, config_dir, target )
    lines = f( dependencies )
    open(path, 'w').write( '\n'.join( lines ) )
    return


class DependencyMissing(Exception):

    def __init__(self, packagename, packageid=None,
                 errormessage=None, suggestion=None):
        self.packagename = packagename
        self.packageid = packageid or packagename
        self.errormessage = errormessage
        self.suggestion = suggestion
        return
    
    pass


class Factory:

    def __init__(self,
                 export_root,
                 build_root,
                 config_dir,
                 target = 'shared,opt',
                 ):
        self.target = target
        self.export_root = export_root
        self.build_root = build_root
        self.config_dir = config_dir
        return


    def __call__(self, dependencies = [ 'Python' ]):
        import os
        config_dir = self.config_dir
        build_root = self.build_root
        export_root = self.export_root
        
        import dottools
        header = dottools.render_header(
            self.target, export_root, build_root, config_dir )

        lines = header
        for dep in dependencies:
            try:
                print "rendering .tools codes for %r ..." % dep
                lines += dottools.render_dependency( dep )
            except InstallationNotFound, err:
                pkgname = err.packagename or dep
                pkgid = err.packageid or dep
                msg = err.errormessage
                if not msg:
                    import traceback
                    msg = traceback.format_exc()
                raise DependencyMissing(
                    pkgname,
                    packageid = pkgid,
                    errormessage = msg,
                    suggestion = err.possible_solution)
            continue
        return lines
        
    pass # end of Factory


from utils.paths.InstallationNotFound import InstallationNotFound

# version
__id__ = "$Id$"

# End of file 
