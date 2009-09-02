
name = 'histogram'
deps = ('pythia', 'stdVector','luban', 'nx5')

import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )
