
setupScript = 'setup_measurement'
name = 'measurement'
sub_modules = None
deps = ('pythia', 'nx5', 'instrument', 'histogram',)
checkoutCmd = "svn co svn://danse.us/measurement"
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
