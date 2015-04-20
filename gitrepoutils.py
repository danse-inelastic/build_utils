"wrapper of git commands"

import os


def checkoutCmd( server, repo, branch, name=None ):
    '''checkoutCmd( "https://github.com/heetuu", "histogram", "master")
    '''
    if name is None: 
        raise ValueError, "name is None"
    cmd = [ "git clone" ]
    cmd.append("-b %(branch)s" % locals())
    cmd.append("%(server)s/%(repo)s.git %(name)s" % locals())
    return ' '.join( cmd )


def repoinfo( repo, branch, server = None, name=None ):
    server = server or "https://github.com/heetuu"
    if name is None: 
        raise ValueError, "name is None"
    path = name # path to the checked-out stuff
    coCmd = checkoutCmd( server, repo, branch, name=name)
    updateCmd = "git pull"
    return path, coCmd, updateCmd
    

def repourl(repo, branch, server = None):
    server = server or "https://github.com/heetuu"
    return "%(server)s/%(repo)s" % locals()

