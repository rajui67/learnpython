import sys
from typing import Any
def strict_equal(first: Any, second: Any) -> bool:
    return True if type(first) == type(second) and first == second else False
