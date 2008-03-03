name = 'hdf5'
server = 'ftp://ftp.hdfgroup.org/HDF5/prev-releases'

def get( version = None, **kwds ):
    if version is None: version = "1.6.5"
    cmds = [
        './configure --prefix=%s --enable-cxx' % install_path,
        'make',
        'make install',
        #the following is for creating shared library
        'cd c++/src',
        "cat Makefile | sed 's/^CFLAGS.*$/CFLAGS= -O2 -fPIC/' | sed 's/^CXXFLAGS.*$/CXXFLAGS= -O2 -fPIC/' | sed '/^LT_LINK_LIB/ s/static/shared/' | sed '/^LT_LINK_EXE/s/static/shared/' > Makefile.new",
        "mv Makefile Makefile.unsedded",
        "mv Makefile.new Makefile",
        "make clean",
        "make",
        "make install",
        ]
                        
    def _():
        install( name, version,
                 server = server,
                 install_commands = cmds,
                 **kwds )
        import os
        os.environ['HDF5_DIR'] = install_path
        return
    
    return _
    

from utils.installers.src import install, install_path

