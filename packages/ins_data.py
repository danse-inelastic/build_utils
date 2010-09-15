name='ins-data'
reponame = 'ins-data'
branch = ''

setupScript = 'setup_ins_data'
path = 'ins-data'
sub_modules = None
deps = tuple()
checkoutCmd = "svn co svn://danse.us/ins-data"
updateCmd = "svn update"


def patch( dest ):
    expandPharosData( os.path.join( dest, "Pharos" ) )
    return


def expandPharosData( path ):
    for item in os.listdir( path ):
        #if not a gzip file, skip
        if not item.endswith( "gz" ): continue
        
        #if already expanded, skip
        orig, ext = os.path.splitext( item )
        if os.path.exists( os.path.join( path, orig ) ):
            os.remove( os.path.join(path, item ) )
            continue

        #unzip
        cmd =  "cd %s; gunzip %s;  cd -" % (
            path, item )
        print cmd
        os.system( cmd )
        continue
    return


import os
