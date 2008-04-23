
name = 'bpext'
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"
branch = "bpext"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
