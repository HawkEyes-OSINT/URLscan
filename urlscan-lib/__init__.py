# __init__.py

from .result import *
from .search import *
from .submissions import *

__all__ = [
    # List all the function names from each module
    *result.__all__,
    *search.__all__,
    *submissions.__all__,
]

