name = 'multiphonon'
reponame = name
branch = ''


setupScript = 'setup_multiphonon'
path = 'multiphonon'
sub_modules = None
deps = ('numpy', 'pylab', 'histogram', 'pythia', 'pyregui', 'wxtools')
checkoutCmd = "svn co svn://danse.us/multiphonon"
updateCmd = "svn update"


def patch( dest ):
    curdir = os.path.abspath( os.path.dirname( __file__ ) )
    patches_dir = os.path.join( curdir, "multiphonon-patches" )
    cp_sqePlot( patches_dir, dest )
    return
    

def cp_sqePlot( patches_dir, dest ):
    import os
    orig = os.path.join(dest, "src", "sqePlot.py" ) 
    patch = os.path.join( patches_dir, "sqePlot.py" )
    cmd = "cp  %s %s" % (patch, orig)
    print "patching...: %s" % cmd
    os.system( cmd )
    return



import os
