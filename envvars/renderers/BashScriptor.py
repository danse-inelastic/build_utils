# -*- python -*-
# Jiao Lin
# Caltech


class BashScriptor(object):

    def render(self, operations):
        self._lines = []
        for op in operations:
            self._lines += op.identify(self)
            continue
        return self._lines


    def onSet(self, op):
        return ['export %s="%s"' % (op.name, op.value)]


    def onAppend(self, op):
        return ['export %s=$%s:"%s"' % (op.name, op.name, op.value)]


    def onPrepend(self, op):
        return ['export %s="%s":$%s' % (op.name, op.value, op.name)]


# $Id$
# end of file
