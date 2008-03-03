
from utils.installers import tarball_path, install_path, execute

def install( name,
             version = None,  revision = None,
             server = None, identifier = None,
             install_commands = [],
             **kwds ):
    if identifier is None:
        identifier = '%s-%s' % (name, version,)
        pass
    tarball = "%s.tar.gz" % identifier
    link = '%s/%s' % (server, tarball )
    path = identifier
    
    cmds = [
        'cd %s' % tarball_path,
        'rm -rf %s %s' % (tarball, path),
        'wget %s'  % link,
        'tar zxvf %s' % tarball,
        'cd %s' % path,
        ]
    cmds += install_commands
    cmd = ';'.join(cmds)
    execute(cmd)
    return
