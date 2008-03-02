"""
handle paths for gnuplot package
"""

name = 'gnuplot'
description = 'gnuplot plotting package'


from FromEnvVariables import PathsFinder 
fromEnvVars = PathsFinder( name, description, hints = "GNUPLOT" )


from FromExecutable import PathsFinder
fromExe = PathsFinder( name, description, hints = {"executable": "gnuplot"} )

toolset  = [fromEnvVars,
            fromExe,]


from search import search
paths = search(toolset)

