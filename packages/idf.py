name = 'idf'
deps = ()

import repoutils
reponame = 'inelastic'
branch = "idf"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
