setupScript = 'setup_mystic'
path = 'mystic'
sub_modules = None
deps = ()
updateCmd = "svn update"
checkoutCmd = "svn co svn://danse.us/mystic"

revision = 43


def patch( dest ):
    curdir = os.path.abspath( os.path.dirname( __file__ ) )
    patches_dir = os.path.join( curdir, "mystic-patches" )
    copy_setup_mystic_py( patches_dir, dest )
    return
    

def copy_setup_mystic_py( patches_dir, dest ):
    #setup_mystic.py cannot be put into mystic
    #so we have to copy it over at this time
    import os
    src = os.path.join( patches_dir, "setup_mystic.py" )
    dst = os.path.join(dest, "setup_mystic.py" )
    print "copy %s to %s" % (src, dst)
    import shutil
    shutil.copy( src, dst )
    return

import os
