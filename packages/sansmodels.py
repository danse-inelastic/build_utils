
name = 'sansmodels'
deps = ()

import repoutils
reponame = 'sans'
branch = "trunk/sansmodels/src"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )
