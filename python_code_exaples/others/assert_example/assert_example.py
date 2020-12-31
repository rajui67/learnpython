import sys
from typing import Any

''' This is just to illustrate the use of the assert statement. strict_equal can be much easily implemented thus so:
    from typing import Any
    def strict_equal(first: Any, second: Any) -> bool:
        return True if type(first) == type(second) and first == second else False
    NOTE: !!!Do not use assertions to for validations as is used here. Assertions are use It is possible to turn assertions off. 
    Assertions may be turned off in production.
    Assertions are meant for quick data validation processes during development, and should never be used for handling errors in production. always raise and catch Exceptions for that.   
'''

def strict_equal(first: Any, second: Any) -> bool:
    assert type(first) == type(second),  'Failed'
    does_it_equal = False
    try:
        does_it_equal = (first == second) 
    except AssertionError as Ae:
        print('Here')
        ex_name, ex_message, ex_stack = sys.exc_info()
        print('ex_message =', ex_message)
        if ex_message == 'Failed':
              does_it_equal = False
        else:
            raise Ae
    return does_it_equal