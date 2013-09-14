name = 'gsl'

def get( version = None, **kwds ):
    if version is None: version = "X.Y.Z"
    major, minor, release = version.split('.')
    server = pre_server 
    
    cmds = [
        './configure --prefix=%s --enable-cxx' % install_path,
        'make',
        'make install',
        ]
                        
    def _():
        install( name, version,
                 server = server,
                 install_commands = cmds,
                 **kwds )
        import os
        os.environ['GSL_DIR'] = install_path
        return
    
    return _
    

from utils.installers.src import install, install_path

