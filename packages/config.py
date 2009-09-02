name = 'config'
deps = []

from utils import repoutils
reponame = 'ctrl'
branch = "config/branches/with_doxygen_and_docbook_support"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo(reponame, branch, name=name)


