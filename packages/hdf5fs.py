name = 'hdf5fs'
sub_modules = None
deps = ('pythia','array_kluge',) #hdf5
revision = "55"
checkoutCmd = "svn co -r %s svn://danse.us/hdf5fs" % revision
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )
