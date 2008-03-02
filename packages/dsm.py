

setupScript = 'setup_dsm'
name = 'dsm'
sub_modules = None
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"
branch = "dsm"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
