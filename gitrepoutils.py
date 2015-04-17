"wrapper of git commands"

import os


def checkoutCmd( server, repo, branch, name=None ):
    '''checkoutCmd( "git@github.com:yxqd", "histogram", "master")
    '''
    if name is None: 
        raise ValueError, "name is None"
    cmd = [ "git clone" ]
    cmd.append("-b %(branch)s" % locals())
    cmd.append("%(server)s/%(repo)s.git %(name)s" % locals())
    return ' '.join( cmd )


def repoinfo( repo, branch, server = None, name=None ):
    server = server or "git@github.com:yxqd"
    if name is None: 
        raise ValueError, "name is None"
    path = name # path to the checked-out stuff
    coCmd = checkoutCmd( server, repo, branch, name=name)
    updateCmd = "git pull"
    return path, coCmd, updateCmd
    

def repourl(repo, branch, server = None):
    server = server or "git@github.com:yxqd"
    return "%(server)s/%(repo)s" % locals()

