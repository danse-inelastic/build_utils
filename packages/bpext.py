
name = 'bpext'
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"

# svn: old
branch = "bpext"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name)

# git
reponame = "bpext"
branch = "master"
path, checkoutCmd, updateCmd = repoutils.git.repoinfo( reponame, branch, name=name )
