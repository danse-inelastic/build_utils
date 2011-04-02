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


def bypostfix(postfix='TestCase.py'):
    """test if a python module is a unittest

    this method assumes that any module ends with the given postfix
    is a unittest module.
    """
    def _(filename):
        return filename.endswith(postfix)
    return _


def byprefix(prefix='Test'):
    """test if a python module is a unittest

    this method assumes that any module starts with the given prefix
    is a unittest module.
    """
    def _(filename):
        return filename.startswith(prefix)
    return _



# version
__id__ = "$Id$"

# End of file 
