name = 'dsm'
deps = []
#'boostpython'
#'scipy'

import repoutils
reponame = "inelastic"
branch = "dsm"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name) 
