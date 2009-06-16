
import os


def checkoutCmd( server, repo, branch, revision=None, name=None ):
    '''checkoutCmd( "svn://danse.us", "histogram", "releases/DRCS-1.2" )
    '''
    if name is None: name = repo
    cmd = [ "svn co" ]
    if revision: cmd.append('-r %s' % revision)
    cmd.append("%(server)s/%(repo)s/%(branch)s %(name)s" % locals())
    return ' '.join( cmd )


def repoinfo( repo, branch, server = "svn://danse.us", revision=None, name=None ):
    if name is None: name = repo
    path = name # path to the checked-out stuff 
    coCmd = checkoutCmd( server, repo, branch, revision=revision, name=name )
    updateCmd = "svn update"
    return path, coCmd, updateCmd
    
    
