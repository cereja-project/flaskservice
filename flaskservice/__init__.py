from cereja.utils import get_version_pep440_compliant
from flaskservice._base import Api, View

VERSION = "0.0.1.final.0"

__version__ = get_version_pep440_compliant(VERSION)
