
name = 'sample'
deps = [] 
checkoutCmd = "svn co svn://danse.us/sample"
updateCmd = "svn update"


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )
