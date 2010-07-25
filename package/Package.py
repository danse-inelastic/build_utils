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


class Package:

    name = None # name 
    deps = None # dependencies 

    repo = None # repository info
    
    patch = None # patch method to apply patch


class Repository:

    'package repository'
    
    checkout_command = None # check out command
    update_command = None # update command
    url = None # url

# version
__id__ = "$Id$"

# End of file 
