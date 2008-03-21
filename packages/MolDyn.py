
name = 'MolDyn'
deps = [] 

import repoutils
reponame = name
branch = "molDynamics"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
