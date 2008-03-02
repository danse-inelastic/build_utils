__doc__ = """
The machinery to find paths of a package.
This module contains the base class.
"""

class PathsFinder:

    mechanism = "Warning: subclass should provide description of the mechanism used to determine the paths of a package"

    def __init__(self, name, description, hints = None, derivedFrom = None):
        """PathsFinder(name, description, hints, derivedFrom) -> an instance of paths finder.
        This paths finder can find paths of a package with given name and description.
        The "hints" provided will be used to search or guess the paths.
        The paths could be derived from other package paths instance. If so, use keyword
          "derivedFrom"
        """
        self.name = name
        self.description = description
        self._hintsToFindPaths = hints
        self._derivedFrom = derivedFrom
        return

    def extract(self):
        '''extract my paths
        '''
        raise NotImplementedError, "%s must override extract" % self.__class__.__name__
    

    def getPaths(self, name):
        from Paths import Paths
        return Paths(name)
