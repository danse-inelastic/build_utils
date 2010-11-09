#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
given a directory, recursively run all unittests and gather statistics
'''

import unittest, os, sys


def isunittestmodule_bypostfix(postfix='TestCase.py'):
    """test if a python module is a unittest

    this method assumes that any module ends with the given postfix
    is a unittest module.
    """
    def _(filename):
        return filename.endswith(postfix)
    return _


def _importModule(name):
    try:
        exec 'import %s as m' % name
    except:
        import traceback
        tb = traceback.format_exc()
        raise ImportError, 'failed to import %s. traceback:\n%s' % (name, tb)
    return m


class SilentTestRunner:

    'run tests silently'

    def run(self, test):
        result = unittest.TestResult()
        test(result)
        return result
    


def runtestsInDir(
    path,
    isunittestmodule=isunittestmodule_bypostfix(),
    testsuitefactory='pysuite',
    testcase='TestCase',
    testrunner = None,
    ):
    """find all unit tests in the directoy of given path
    (no recursion) and add them in one
    test suite, and run the suite
    """
    #
    pwd = os.path.abspath(os.curdir)
    path = os.path.abspath(path)
    os.chdir(path)
    if path not in sys.path:
        syspath_restore = list(sys.path)
        sys.path = [path] + sys.path
    else:
        syspath_restore = None

    def _restore():
        if syspath_restore:
            sys.path = syspath_restore
        os.chdir(pwd)

    # the suite of everything
    suite = unittest.TestSuite()

    # the modules for unittests
    entries = os.listdir(os.curdir)
    testmodules = filter(isunittestmodule, entries)
    modnames = [f[:-3] for f in testmodules if f.endswith('.py')]
    testmodules = map(_importModule, modnames)

    if not testmodules:
        _restore()
        return

    #
    _standalonetestmodules = []
    _skipped = []
    #
    import warnings
    for m in testmodules:
        if hasattr(m, 'standalone'):
            _standalonetestmodules.append(os.path.join(path, m.__file__))
            continue
        if hasattr(m, 'skip'):
            _skipped.append(os.path.join(path, m.__file__))
            continue
        if hasattr(m, testsuitefactory):
            f = getattr(m, testsuitefactory)
            suite1 = f()
        elif hasattr(m, testcase):
            t = getattr(m, testcase)
            suite1 = unittest.makeSuite(t)
        else:
            warnings.warn("Don't know how to extract test suite out of %s" % m)
            continue
        suite.addTest(suite1)
        continue

    if testrunner is None:
        # testrunner = unittest.TextTestRunner(verbosity=0)
        testrunner = SilentTestRunner()
        
    ret = testrunner.run(suite)

    _restore()

    if ret.testsRun:
        res = _formatResult(ret)
        res.standaloneTests += _standalonetestmodules
        res.skippedTests += _skipped

    elif _standalonetestmodules or _skipped:
        res = Result()
        res.standaloneTests = _standalonetestmodules
        res.skippedTests = _skipped
    else:
        res = None
    return res



def _formatResult(result):
    '''convert unittest TestResult instance to instance of Result class
    in this module.

    inputs:
     - result: unittest.TestResult instance

    output:
     - instance of Result
    '''
    res = Result()
    res.testsRun = result.testsRun
    res.errors = [_formatFailure(f) for f in result.errors]
    res.failures = [_formatFailure(f) for f in result.failures]
    return res


def _formatFailure(failure):
    method, tb = failure
    return method.shortDescription(), tb
    

class Result:

    def __init__(self):
        self.testsRun = 0
        self.failures = []
        self.errors = []
        self.timeTaken = 0
        self.standaloneTests = []
        self.skippedTests = []
        

    def __iadd__(self, result):
        self.testsRun += result.testsRun
        self.failures += result.failures
        self.errors += result.errors
        self.standaloneTests += result.standaloneTests
        self.skippedTests += result.skippedTests
        return self


def fn_match_patterns(name, patterns):
    import fnmatch
    for pattern in patterns:
        if fnmatch.fnmatch(name, pattern): return True
        continue
    return False


def path_match_patterns(path, patterns):
    names = path.split('/')
    for name in names:
        if fn_match_patterns(name, patterns): return True
        continue
    return False


def runtests(path, exclude_dirs=[]):
    '''run unittests recursively and return a Result instance
    '''
    import fnmatch
    result = Result()
    import time
    start = time.time()
    for dirpath, dirnames, filenames in os.walk(path):
        if exclude_dirs and path_match_patterns(dirpath, exclude_dirs):
            continue
        for dir in dirnames:
            if exclude_dirs and fn_match_patterns(dir, exclude_dirs):
                continue
            path1 = os.path.join(dirpath, dir)
            r = runtestsInDir(path1)
            if r:
                result += r
        continue
    r = runtestsInDir(path)
    stop = time.time()
    timeTaken = stop-start
    if r:
        result += r

    result.timeTaken = timeTaken
    return result


# copied from unittest.py
class _WritelnDecorator:
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        self.stream = stream

    def __getattr__(self, attr):
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        if arg: self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed


def printRsult(result, stream = None):
    if not stream:
        stream = sys.stdout
    stream = _WritelnDecorator(stream)
        
    for desc, tb in result.errors:
        stream.writeln('='*70)
        stream.writeln('ERROR: %s' % desc)
        stream.writeln('-'*70)
        stream.write(tb)
        print
        
    for desc, tb in result.failures:
        stream.writeln('='*70)
        stream.writeln('FAILED: %s' % desc)
        stream.writeln('-'*70)
        stream.write(tb)
        print
        
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

    if result.standaloneTests:
        # run standalone tests in sub-processes
        import subprocess as sp
        stream.writeln()
        stream.writeln('-' * 70)
        stream.writeln('%s standalone tests.' % len(result.standaloneTests))
        stream.writeln('Run them one by one')
        failures = []
        for t in result.standaloneTests:
            path, filename = os.path.split(t)
            cmd = 'cd %s && python %s' % (path, filename)
            stream.writeln(' - running %s...' % cmd)
            p = sp.Popen(cmd, stdout=stream, stderr=stream, shell=True)
            p.communicate()
            rt = p.wait()
            if rt: failures.append(t)
            continue
        result.failures += failures
        stream.writeln()
        stream.writeln('-' * 70)
        stream.writeln('Ran %s standalone tests.' % len(result.standaloneTests))
        if failures:
            stream.writeln('FAILED (errors=%s)' % len(failures))
        else:
            stream.writeln('SUCCEED')
            

    if result.skippedTests:
        stream.writeln()
        stream.writeln('-' * 70)
        stream.writeln('Skipped %s tests.' % len(result.skippedTests))
        for t in result.skippedTests:
            stream.writeln(' - %s' % t)
            continue
    return


# version
__id__ = "$Id$"

# End of file 
