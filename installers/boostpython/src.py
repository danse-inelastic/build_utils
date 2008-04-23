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


name = 'boostpython'
server = 'http://superb-east.dl.sourceforge.net/sourceforge/boost'

def get( version = None, **kwds ):
    name = 'boost'
    if version is None: version = "1_35_0"
    identifier = "%s_%s" % (name, version)
    
    install_cmds = [
        './configure --prefix=%s --with-libraries=python' %  (install_path,),
        'make install',
        ]

    from utils.installers.misc import so
    postinstall_cmds = [
        'cd %s/include' % (install_path,),
        'ln -s %(name)s-%(version)s/%(name)s %(name)s' % {
        'name': name,
        'version': version,
        },
        'cd %s/lib' % (install_path,),
        'ln -s libboost_python-%(version)s.%(so)s libboost_python.%(so)s' % {
        'version': version,
        'so': so,
        },
        ]

    cmds = install_cmds + postinstall_cmds

    def _():
        install(
            name, version,
            identifier = identifier,
            server = server,
            install_commands = cmds,
            **kwds )

        # notification
        import os
        os.environ['BOOSTPYTHON_DIR'] = install_path
        
        return
    
    return _
    

from utils.installers.src import install, install_path



# version
__id__ = "$Id$"

# End of file 
