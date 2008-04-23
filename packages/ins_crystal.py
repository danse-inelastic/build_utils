
name = 'ins_crystal'
deps = [] 

import repoutils
reponame = 'inelastic'
branch = "crystal"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
