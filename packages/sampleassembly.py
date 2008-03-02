
setupScript = 'setup_sampleassembly'
name = 'sampleassembly'
sub_modules = None
deps = [] 

import repoutils
reponame = 'inelastic'
branch = "sample/branches/sampleassembly"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
