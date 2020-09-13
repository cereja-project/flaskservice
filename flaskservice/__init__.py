from cereja.utils import get_version_pep440_compliant
from flaskservice.base import Api, View

VERSION = "0.0.1.alpha.0"

__version__ = get_version_pep440_compliant(VERSION)
