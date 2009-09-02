name = 'stdVector'
sub_modules = None
deps = ('numpy','pythia','array_kluge')
checkoutCmd = "svn co svn://danse.us/stdVector"
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )

