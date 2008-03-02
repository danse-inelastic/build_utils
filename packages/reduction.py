

setupScript = 'setup_reduction'
name = 'reduction'
sub_modules = None
deps = 'pythia', 'stdVector', 'nx5', 'measurement', 'histogram', 'instrument', 'pyregui', 'wx'
#'scipy'
checkoutCmd = "svn co svn://danse.us/reduction"
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
