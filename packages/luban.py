name = 'luban'
sub_modules = None
deps = 'pythia',


import repoutils
reponame = 'pyregui'
branch = "trunk/luban"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=name )

