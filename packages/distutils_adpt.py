
setupScript = 'setup_distutils_adpt'
name = 'distutils-adpt'
sub_modules = None
deps = ('distutils',)


import repoutils
reponame = name
branch = "trunk"
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch )

