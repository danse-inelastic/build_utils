name = 'config'
deps = []

from utils import repoutils

# svn: old
reponame = 'ctrl'
branch = "config/branches/with_doxygen_and_docbook_support"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo(reponame, branch, name=name)

# git
reponame = "danse-config"
branch = "master"
path, checkoutCmd, updateCmd = repoutils.git.repoinfo( reponame, branch, name=name )
