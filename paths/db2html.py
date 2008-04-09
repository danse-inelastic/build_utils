"""
handle paths for db2html xsl
"""

name = 'db2html'
description = 'docbook->html xsl'

from FromEnvVariables import PathsFinder 

fromEnvVars = PathsFinder( name, description, hints = "DB2HTML_XSL" )

toolset  = [fromEnvVars,]

from search import search
paths = search(toolset)

