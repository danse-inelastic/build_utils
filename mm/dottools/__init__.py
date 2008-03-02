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

def render_header( target, export_root, build_root, config_dir ):
    lines = render_target(target) + \
            render_export_root( export_root ) + \
            render_build_root( build_root ) + \
            render_config_path( config_dir )
    return lines


def render_dependency( dep ):
    exec 'from utils.paths.%s import paths' % dep in locals()
    from dependencies import render
    return render(paths)
    

def render_target( target ):
    return ['export TARGET=%s' % target]


def render_export_root( export_root ):
    return ['export EXPORT_ROOT="%s"' % export_root]


def render_build_root( build_root ):
    return ['export BLD_ROOT="%s"' % build_root]


def render_config_path( config_dir ):
    return [
        'export PATH=%s/make:${PATH}' % config_dir,
        'export BLD_CONFIG="%s"' % config_dir,
        ]


# version
__id__ = "$Id$"

# End of file 
