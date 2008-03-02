#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2006 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# This directory contains python modules describing packages to be included
# in the software.
#
# __init__.py: gather global information about packages. don't touch
# bundles.py: packages are grouped into bundles. change it when new packages
#             are added or when bundles need to be restructured
# defaults.py: default packages to be installed
# other modules: each module contains information about a specific package
#
#   setupScript = name of distutils-adpt setup script
#   path = path in 'src' directory
#   sub_modules = names of sub modules (This is usually None. Only useful for DANSE:graphics)
#   deps = names of dependencies
#   checkoutCmd = command to check out the package from repository


from bundles import *

from defaults import *


packageSequence = []
for name in bundleNames: packageSequence += bundleInfo[name]

#alias
packageNames = packageSequence


def createTable(packageNames):
    import sys, os
    t = {}
    for name in packageNames:
        modname = name.replace( '-', '_' )
        m = __import__( "packages.%s" % modname, globals(), locals(), [""] )
        t[name] = m.__dict__
        continue
    return t
                    
        

#a dictionary of infos of packages
#   name: (setup script name,  relative path of the package, sub modules, dependencies)
packageInfoTable = createTable( packageNames )
    

# modules is a dictionary of { package: sub_modules }
modules = {}
for name in packageNames: modules[name] = packageInfoTable[ name ]['sub_modules']


def checkout( packageNames, dest ):
    """check out packages at "dest" directory"""
    for package in packageNames:
        cmd = "cd %s; " % dest
        info = packageInfoTable[ package ]
        cocmd = info['checkoutCmd']
        if cocmd:
            cmd += cocmd
            if os.system(cmd): print "Unable to check out %s" % package
            pass
        patch(package, dest)
        continue
    return


def update( packageNames, dest ):
    """update packages at "dest" directory"""
    import os
    for package in packageNames:
        info = packageInfoTable[ package ]
        p = os.path.join( dest, info['path'] )
        cmd = "cd %s; " % p
        udcmd = info['updateCmd']
        if udcmd:
            cmd += udcmd
            if os.system(cmd): print "Unable to update %s" % package
            pass
        patch(package, dest)
        continue
    return


def patch( packageName, dest ):
    info = packageInfoTable[ packageName ]
    patch = info.get( 'patch' )
    if patch: 
        path = info['path']
        d = os.path.join( dest, path )
        patch(d)
    else: "No patch for package %s" % packageName
    return


import os


# version
__id__ = "$Id$"


# End of file 
