#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# this module differs from utils.svnrepoutils in that
# this module tries to bind with object utils.package.Package.Repository.


from utils.svnrepoutils import checkoutCmd, repourl

update_command = 'svn update'

def getPackageRepository(
    repo, branch, 
    server = "svn://danse.us", revision=None, name=None):
    '''getPackageRepository(repo, branch, server,...) -> Package.Repository instance

repo: name of repository for the package
branch: branch in the repository for the package
server: server of the repository
revision: revision of the repository
name: name of the package. default to be the same as repo

Eg.:
 
 >>> getPackageRepository(
         "luban", "trunk", 
         server = "svn://danse.us", name = "luban")

'''
    from ..Package import Repository
    r = Repository()
    r.checkout_command = checkoutCmd(
        server, repo, branch, revision=revision, name=name )
    r.update_command = update_command
    r.url = repourl(repo, branch, server=server)
    r.name = repo
    r.pkgname = name or repo
    r.branch = branch
    r.server = server
    r.revision = revision
    r.type = 'svn'
    return r



def getRevision(pkgrepo):
    from utils.svnrepoutils import get_revision
    reponame = pkgrepo.name
    branch = pkgrepo.branch
    server = pkgrepo.server
    return get_revision('/'.join([reponame, branch]), server=server)


# version
__id__ = "$Id$"

# End of file 