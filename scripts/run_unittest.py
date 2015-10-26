#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2014  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from utils.unittest.run_tests import \
    Result, iterdirs, runtestsInDir, _WritelnDecorator
import pickle, os, subprocess as sp, sys, shlex
import time, datetime

def run(path, exclude_dirs=None, skip_long_tests=None, log=None):
    # run unit tests in each path
    # here we run each test in a subprocess, so that we can
    # harness the outputs.
    # this is different from utils.unittest.run_tests.runtests method
    result = Result()
    print "%s: Recurively run all unit tests" % datetime.date.today()
    
    start = time.time()
    execpath = sys.argv[0]
    log = log and open(log, 'wt')
    def run1(p1, skip_long_tests=False):
        cmd = ['python', execpath, p1,
               '--report=false', 
               '--skip-long-tests' if skip_long_tests else '']
        cmd = ' '.join(cmd)
        process = sp.Popen(shlex.split(cmd), stdout=log, stderr=log)
        rt = process.wait()
        return pickle.load(open(res_pkl(p1)))
    
    # sys.stdout.write('* working ')
    for p1 in iterdirs(path, exclude_dirs=exclude_dirs):
        # sys.stdout.write('.')
        # sys.stdout.flush()
        sys.stdout.write('* running in '+p1)
        sys.stdout.flush()
        start1 = time.time()
        r = run1(p1, skip_long_tests=skip_long_tests)
        if r:
            result += r
        end1 = time.time()
        elapsed = end1-start1
        sys.stdout.write(" ... took %s" % secondsToStr(elapsed))
        if elapsed > 180:
            sys.stdout.write(" (Long test!!!)")
        sys.stdout.write("\n")
        continue
    sys.stdout.write('\n')
    sys.stdout.flush()
    
    r = run1(path, skip_long_tests=skip_long_tests)
    if r: result += r
    result += runStandAloneTests(result.standaloneTests, log)
    
    stop = time.time()
    timeTaken = stop-start
    
    result.timeTaken = timeTaken
    return result


def secondsToStr(t):
    rediv = lambda ll,b : list(divmod(ll[0],b)) + ll[1:]
    return "%d:%02d:%02d.%03d" % tuple(reduce(rediv,[[t*1000,],1000,60,60]))


res_pkl = lambda path: os.path.join(path, '.test-res.pkl')
def run1(path, **kwds):
    # run unit tests in the given path. no-recursion
    # print '*', path
    res = runtestsInDir(path, **kwds)
    resfile = res_pkl(path)
    pickle.dump(res, open(resfile, 'w'))
    return res


def runStandAloneTests(tests, log):
    errors = []
    print "** Standalone tests"
    for t in tests:
        start1 = time.time()
        
        sys.stdout.write("* Running %s" % t); sys.stdout.flush()
        rt, out, err = runStandAloneTest(t, log)
        if rt:
            errors.append((t, err))
            
        end1 = time.time()
        elapsed = end1-start1
        sys.stdout.write(" ... took %s" % secondsToStr(elapsed))
        if elapsed > 180:
            sys.stdout.write(" (Long test!!!)")
        sys.stdout.write("\n"); sys.stdout.flush()
        continue
    res = Result()
    res.testsRun = len(tests)
    res.errors = errors
    return res
        

def runStandAloneTest(t, log):
    path, filename = os.path.split(t)
    cmd = 'cd %s && python %s' % (path, filename)
    p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    out, err = p.communicate()
    return p.returncode, out, err

    
def printResult(result, stream = None):
    if not stream:
        stream = sys.stdout
    stream = _WritelnDecorator(stream)
        
    for desc, tb in result.errors:
        stream.writeln('='*70)
        stream.writeln('ERROR: %s' % desc)
        stream.writeln('-'*70)
        stream.write(tb)
        stream.writeln('')
        
    for desc, tb in result.failures:
        stream.writeln('='*70)
        stream.writeln('FAILED: %s' % desc)
        stream.writeln('-'*70)
        stream.write(tb)
        stream.writeln('')
        
    stream.writeln('-' * 70)
    stream.writeln('Ran %s tests in %ss' % (result.testsRun, result.timeTaken))
    stream.writeln()
    
    if result.errors or result.failures:
        stream.write("FAILED (")
        failed, errored = map(len, (result.failures, result.errors))
        if failed:
            stream.write("failures=%d" % failed)
        if errored:
            if failed: stream.write(", ")
            stream.write("errors=%d" % errored)
        stream.writeln(")")
    else:
        stream.writeln("OK")

    if result.skippedTests:
        stream.writeln()
        stream.writeln('-' * 70)
        stream.writeln('Skipped %s tests.' % len(result.skippedTests))
        for t in result.skippedTests:
            stream.writeln(' - %s' % t)
            continue

    stream.writeln( '____' )
    stream.writeln( '')
    if result.errors or result.failures:
        sys.exit(1)
    return


def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "", "--skip-long-tests", 
        action="store_true", dest="skip_long_tests",
        )
    def tolist(option, opt, value, parser):
        setattr(parser.values, option.dest, value.split(','))
    parser.add_option(
        "", "--exclude-dirs",
        type = "string",
        action = "callback",
        dest = 'exclude_dirs',
        callback = tolist,
        )
    parser.add_option(
        '-r', "--recursive",
        action="store_true", dest="recursive",
        )
    parser.add_option('', '--log', dest = 'log',)
    def toboolean(option, opt, value, parser):
        trues = ['true', 'yes', 'on']
        falses = ['false', 'no', 'off']
        assert value in trues+falses, "Invalid input: %s" % value
        setattr(parser.values, option.dest, value.lower() in trues)
    parser.add_option(
        '', '--report', dest = 'report', default = True, type="string",
        action = 'callback', callback = toboolean)
    
    (options, args) = parser.parse_args()
    
    assert len(args) == 1
    path = args[0]
    
    if options.recursive:
        res = run(
            path, 
            skip_long_tests=options.skip_long_tests, 
            exclude_dirs=options.exclude_dirs,
            log = options.log,
            )
    else:
        res = run1(path, skip_long_tests=options.skip_long_tests)

    if options.report:
        print '*'*60
        printResult(res)
    return



# version
__id__ = "$Id$"

# End of file 
