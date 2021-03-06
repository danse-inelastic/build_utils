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


from utils.svnrepoutils import checkoutCmd, updateCmd, repourl

default_repo_server = 'svn://danse.us'
#default_repo_server = 'svn+ssh://svn@danse.us'

def getPackageRepository(
    repo, branch, 
    server = None, revision=None, name=None):
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
    if server is None: server = default_repo_server
    from ..Package import Repository
    r = Repository()
    r.checkout_command = checkoutCmd(
        server, repo, branch, revision=revision, name=name )
    r.update_command = updateCmd(revision=revision)
    r.url = repourl(repo, branch, server=server)
    r.name = repo
    r.pkgname = name or repo
    r.branch = branch
    r.server = server
    r.revision = revision
    r.type = 'svn'
    r.getRevInUse = lambda :getRevInUse('src/%s/' % r.pkgname)
    return r


def getRevInUse(path):
    """get revision number in use for the given path"""
    cmd = 'svn info %s' % path
    import subprocess as sp
    out = sp.check_output(cmd.split())
    sig = 'Revision:'
    for l in out.splitlines():
        if l.startswith(sig):
            return l[len(sig):].strip()
    raise RuntimeError("Should not reach here")


def getRevision(pkgrepo):
    from utils.svnrepoutils import get_revision
    reponame = pkgrepo.name
    branch = pkgrepo.branch
    server = pkgrepo.server
    return get_revision('/'.join([reponame, branch]), server=server)


# version
__id__ = "$Id$"

# End of file 
