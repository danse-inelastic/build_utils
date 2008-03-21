
name = 'sampleassembly'
deps = ['instrument'] 

import repoutils
reponame = 'common'
branch = "dataObjects/sample/branches/sampleassembly"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
