
setupScript = 'setup_histogram'
name = 'histogram'
sub_modules = None
deps = ('pythia', 'stdVector','luban', 'nx5')
checkoutCmd = "svn co svn://danse.us/histogram"
updateCmd = "svn update"
    

import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
