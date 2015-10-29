#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2014 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# this module differs from utils.gitrepoutils in that
# this module tries to bind with object utils.package.Package.Repository.


import utils.gitrepoutils as gru

default_repo_server = 'https://github.com/danse-inelastic'

def getPackageRepository(
    repo, branch, 
    server = None, revision=None, 
    name=None):
    '''getPackageRepository(repo, branch, server,...) -> Package.Repository instance

repo: name of repository for the package
branch: branch in the repository for the package
server: server of the repository
revision: revision of the repository
name: name of the package. default to be the same as repo

Eg.:
 
 >>> getPackageRepository(
         "luban", "trunk", 
         server = "https://github.com/danse-inelastic", name = "luban")

'''
    if server is None: server = default_repo_server
    from ..Package import Repository
    r = Repository()
    # how about revision?
    path, coCmd, updateCmd = gru.repoinfo(
        repo, branch, server=server, name=name) 
    
    r.checkout_command = coCmd
    r.update_command = updateCmd
    r.url = gru.repourl(repo, branch, server=server)
    r.name = repo
    r.pkgname = name or repo
    r.branch = branch
    r.server = server
    r.revision = revision
    r.type = 'git'
    r.getRevInUse = lambda :getRevInUse('src/%s/' % r.pkgname)
    return r


def getRevInUse(path):
    """get revision number in use for the given path"""
    cmd = 'git rev-parse HEAD'
    import subprocess as sp
    out = sp.check_output(cmd.split(), cwd=path)
    return out.strip()


# version
__id__ = "$Id$"

# End of file 
