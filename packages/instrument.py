
setupScript = 'setup_instrument'
name = 'instrument'
sub_modules = None
deps = 'pythia', 'nx5','stdVector'
checkoutCmd = "svn co svn://danse.us/instrument"
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
