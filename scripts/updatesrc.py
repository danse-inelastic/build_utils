#!/usr/bin/env python
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


# script to check out sources

def update(names, pkgcontainer, tree):
    srcRt = tree.search( "sources" ).path
    if names:
        packages = [pkgcontainer.getPackage(n) for n in names]
    else:
        packages = pkgcontainer.getAll()
    from ..packages import update
    update(packages, srcRt)
    # import dereference
    # dereference.dereference_recursively( 'src' )
    return


def main(pkgcontainer, releaser_tree):
    '''main function
    
    - pkgcontainer: the container of packages. must have the API defined in utils.packages.Packages
    - releaser_tree: directory tree structure of the releaser
    
    '''
    from optparse import OptionParser
    parser = OptionParser()
    (options, args) = parser.parse_args()
    names = args
    update(names, pkgcontainer, releaser_tree)
    return


def main2(packages_pypkg, releaser_tree):
    '''main function
    
    - packages_pypkg: the python package that has modules describing source packages
    - releaser_tree: directory tree structure of the releaser
    '''
    from ..packages.factories import fromPyPackage
    pkgcontainer = fromPyPackage.factory(packages_pypkg)
    return main(pkgcontainer, releaser_tree)


# version
__id__ = "$Id$"

# End of file 
