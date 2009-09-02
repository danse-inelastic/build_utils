
name = 'instrument'
deps = ['pythia',]

import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name)
