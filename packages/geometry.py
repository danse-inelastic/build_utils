
name = 'geometry'
deps = ['pyre'] 

import repoutils
reponame = 'common'
branch = "geometry/trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name)
