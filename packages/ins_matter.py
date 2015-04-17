
name = 'ins_matter'
deps = [] 

from utils.package import repoutils

# old: svn
# reponame = 'inelastic'
# branch = "crystal/matter"
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

reponame = "matter"
branch = "master"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
