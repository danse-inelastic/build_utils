# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

def load(path):
    env = {}
    s = open(path).read()
    exec s in env

    import testmod_filters
    if 'prefix' in env:
        testmod_filter = testmod_filters.byprefix(env['prefix'])

    if 'postfix' in env:
        testmod_filter = testmod_filters.bypostfix(env['postfix'])

    return {
        'testmod_filter': testmod_filter
        }


# version
__id__ = "$Id$"

# End of file 
