
name = 'ins_matter'
deps = [] 

from utils.package import repoutils
reponame = 'inelastic'
branch = "crystal/matter"
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
