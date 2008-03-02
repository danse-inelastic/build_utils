#!/usr/bin/env python

def preparePackage( package, sourceRoot = "." ):
    package.changeRoot( sourceRoot )
    
    #--------------------------------------------------------
    # now add subpackage journal
    #
    #journal
    package.addPurePython(
        sourceDir = 'python',
        destModuleName = 'mystic' )

    return package



if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('mystic', '0.1')

    preparePackage( package )

    package.setup()

