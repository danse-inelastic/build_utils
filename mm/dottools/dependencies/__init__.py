#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def render( paths ):
    name = paths.name
    try:
        exec "import %s as module" % (name,)
    except ImportError:
        raise NotImplementedError, name
    try: render = getattr(module, 'render')
    except AttributeError:
        raise NotImplementedError, name
    return render( paths )
    

# version
__id__ = "$Id$"

# End of file 
