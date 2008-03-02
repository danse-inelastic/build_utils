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

# make-dottools.py <directory>


def main():
    import sys
    path = sys.argv[0]
    render( path )
    return
    

def render( path, export_root, build_root, config_dir ):
    import os
    
    from deps import externPackageInfo as info
    dependencies = ['Python'] + info.keys()

    path = os.path.join( path, 'dottools' )
    from utils.mm.dottools_factory import render_file
    render_file( path, dependencies,
                 export_root, build_root, config_dir,
                 )
    return path


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 


