name = 'drchops'
deps = 'histogram',
reponame = 'DrChops'
branch = "trunk"

from utils.package import repoutils
repo = repoutils.svn.getPackageRepository(
    reponame, branch, name=name )

