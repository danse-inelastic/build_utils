
setupScript = 'setup_nx5'
name = 'nx5'
sub_modules = None
deps = ('pythia', 'hdf5fs',
        'array_kluge', 'stdVector',)
checkoutCmd = "svn co svn://danse.us/nx5"
updateCmd = "svn update"
    

import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch,name=name)
