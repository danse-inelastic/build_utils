

setupScript = 'setup_numpyext'
name = 'numpyext'
sub_modules = None
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"
branch = "numpyext"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
