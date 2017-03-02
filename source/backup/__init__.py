__version__ = '1.2.1'
__copyright__ = "Vladimir Kushnir aka Kvantum i(c)2017"

import sys
if sys.version_info[:2] < (2, 7):
    raise RuntimeError('PySMI requires Python 2.7 or later')
