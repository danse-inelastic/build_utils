
from utils.installers import tarball_path, install_path, execute

def install( name,
             version = None,  revision = None,
             server = None, identifier = None,
             install_commands = [],
             tarball_ext = 'tar.gz',
             tarball_extraction_cmd = 'tar zxvf',
             **kwds ):
    if identifier is None:
        identifier = '%s-%s' % (name, version,)
        pass
    tarball = "%s.%s" % (identifier, tarball_ext)
    link = '%s/%s' % (server, tarball )
    path = identifier
    
    cmds = [
        'cd %s' % tarball_path,
        'rm -rf %s' % path,
        'rm -rf %s' % tarball,
        'wget %s'  % link,
        '%s %s' % (tarball_extraction_cmd, tarball),
        'cd %s' % path,
        ]
    cmds += install_commands
    cmd = ' && '.join(cmds)
    execute(cmd)
    return
