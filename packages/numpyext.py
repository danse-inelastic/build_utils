name = 'numpyext'
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"
branch = "numpyext"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )
