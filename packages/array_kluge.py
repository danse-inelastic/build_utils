name = 'array_kluge'

setupScript = 'setup_array_kluge'
sub_modules = None
deps = ('pythia',)

import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )

