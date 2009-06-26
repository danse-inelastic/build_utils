name = 'mcvine'
deps = ('dsm', 'numpyext', 'bpext', 
        'histogram', 'instrument', 'sampleassembly', 'pythia', 
        'ins_crystal', # temporarily
        'sansmodels', # optionally
	)

import repoutils
reponame = 'MCViNE'
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name)

