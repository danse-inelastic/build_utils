
name = 'pyregui'
deps = 'pythia',

from utils import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
