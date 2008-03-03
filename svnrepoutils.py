
import os


def checkoutCmd( repo, name, branch ):
    '''checkoutCmd( "svn://danse.us", "histogram", "releases/DRCS-1.2" )
    '''
    cmds = [
        "svn co -N %s/%s" % ( repo, name ),
        "cd %s" % name,
        ]
    leaves = branch.split( '/' )
    for p in leaves[:-1]:
        cmd = "svn up -N %s && cd %s" % (p, p)
        cmds.append( cmd )
        continue
    cmds.append( 'svn up %s' % leaves[-1] )

    return ' && '.join( cmds )


def repoinfo( name, branch, repo = "svn://danse.us" ):
    path = os.path.join( name, branch ) # path to the checked-out stuff 
    coCmd = checkoutCmd( "svn://danse.us", name, branch )
    updateCmd = "svn update"
    return path, coCmd, updateCmd
    
    
