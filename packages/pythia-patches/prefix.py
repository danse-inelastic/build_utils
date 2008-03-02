import os
from install_info import etc

_SYSTEM_ROOT = etc
_USER_ROOT = os.path.join(os.path.expanduser('~'), '.pyre')
_LOCAL_ROOT = [ '.' ]

