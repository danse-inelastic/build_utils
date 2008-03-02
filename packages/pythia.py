
setupScript = 'setup_pythia'
path = 'pythia-0.8'
sub_modules = None
deps = ("config",)

cocmds = [
    'echo',
    'echo ">>> Note <<<"',
    'echo   Enter \\"pyre\\" as the password when prompted',
    'echo',
    "cvs -d :pserver:pyre@cvs.cacr.caltech.edu:/pyre login",
    "cvs -d :pserver:pyre@cvs.cacr.caltech.edu:/pyre co pythia-0.8",
    ]
checkoutCmd = '; '.join( cocmds )
updateCmd = "cvs update"

def patch( dest ):
    curdir = os.path.abspath( os.path.dirname( __file__ ) )
    patches_dir = os.path.join( curdir, "pythia-patches" )
    copy_setup_pythia_py( patches_dir, dest )
    copy_prefix_py( patches_dir, dest )
    apply_journal_patch( patches_dir, dest )
    apply_pyre_patch( patches_dir, dest )
    apply_mpi_patch( patches_dir, dest )
    return
    

def copy_setup_pythia_py( patches_dir, dest ):
    #setup_pythia.py cannot be put into pythia
    #so we have to copy it over at this time
    #pretty weird, I guess
    import os
    src = os.path.join( patches_dir, "setup_pythia.py.template" )
    dst = os.path.join(dest, "setup_pythia.py" )
    import shutil
    print "copy %s to %s" % (src, dst)
    shutil.copy( src, dst )
    return


def copy_prefix_py( patches_dir, dest ):
    import os
    import shutil
    src = os.path.join( patches_dir, "prefix.py" )
    dst = os.path.join( dest, "packages", "pyre", "pyre", 
                        "inventory", "odb", "prefix.py" )
    print "copy %s to %s" % (src, dst)
    shutil.copy( src, dst )

    src = os.path.join( patches_dir, "pyre-inventory-odb-Make.mm" )
    dst = os.path.join( dest, "packages", "pyre", "pyre", 
                        "inventory", "odb", "Make.mm" )
    print "copy %s to %s" % (src, dst)
    os.system( 'rm -f %s' % dst)
    shutil.copy( src, dst )
    return


def apply_journal_patch( patches_dir, dest ):
    import os
    srcs = [
        'manip-templated.h',
        'Diagnostic.h',
        'Diagnostic.icc',
        ]
    for src in srcs:
        orig = os.path.join(
            dest, "packages", "journal", 
            "libjournal", src )
        patch = os.path.join(
            patches_dir, "libjournal-%s.patch" % src )
        cmd = "patch -N  %s %s" % (orig, patch)
        print "patching...: %s" % cmd
        os.system( cmd )
        continue
    return


def apply_pyre_patch(patches_dir, dest ):
    import os
    orig = os.path.join(dest, "packages", "pyre", 
         "pyre", "odb", "fs", "FileLocking.py" )
    patch = os.path.join( patches_dir, "pyre-odb-fs-FileLocking.patch" )
    cmd = "patch -N  %s %s" % (orig, patch)
    print "patching...: %s" % cmd
    os.system( cmd )
    return 


def apply_mpi_patch(patches_dir, dest ):
    import os
    orig = os.path.join(dest, "packages", "mpi" )
    patch = os.path.join( patches_dir, "mpi.patch" )
    cmd = "cd %s && patch -N -p1 < %s && cd -" % (orig, patch)
    print "patching...: %s" % cmd
    os.system( cmd )
    return 


import os
