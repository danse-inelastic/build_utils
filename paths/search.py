
def search( pathsFinders=[] ):
    """search for package with packageName and description 
    """
    errorMsgs = []
    for pathsFinder in pathsFinders:
        try:
            paths = pathsFinder.extract()
            return paths
        except Exception, msg:
            errorMsgs.append( '\n*** Unable to find package %s, the %r.\n -> The search engine used is %r.\n -> The reason of failing is \n"""\n%s\n"""\n' %(pathsFinder.name, pathsFinder.description, pathsFinder.mechanism, msg) )
        continue
    
    #nothing useful found. raise error
    from operator import add
    raise InstallationNotFound, reduce(add, errorMsgs)

from InstallationNotFound import InstallationNotFound
            
        

            
