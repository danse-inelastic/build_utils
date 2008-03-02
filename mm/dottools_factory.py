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
            lines += dottools.render_dependency( dep )
            continue
        return lines
        
    pass # end of Factory



# version
__id__ = "$Id$"

# End of file 
