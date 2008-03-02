

setupScript = 'setup_bpext'
name = 'bpext'
sub_modules = None
deps = []
#'boostpython'
#'scipy'


import repoutils
reponame = "inelastic"
branch = "bpext"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
