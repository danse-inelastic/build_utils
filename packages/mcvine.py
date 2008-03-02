
setupScript = 'setup_mcvine'
name = 'mcvine'
sub_modules = None
deps = ('dsm', 'bpext', 'histogram', 'instrument', 'sampleassembly', 'pythia',)

import repoutils
reponame = 'MCViNE'
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )

