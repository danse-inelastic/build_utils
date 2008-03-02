

setupScript = 'setup_pyregui'
name = 'pyregui'
sub_modules = None
deps = 'pythia',
checkoutCmd = "svn co svn://danse.us/pyregui"
updateCmd = "svn update"


from utils import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
