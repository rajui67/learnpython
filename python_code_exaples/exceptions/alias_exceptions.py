import sys

'''

None of the code snippets will work. Reason as follows

except-foo-as-bar-causes-bar-to-be-removed-from-scope 1 => https://stackoverflow.com/questions/52965952/except-foo-as-bar-causes-bar-to-be-removed-from-scope
scope-of-caught-exception-instance-in-python-2-and-3 => https://stackoverflow.com/questions/44258903/scope-of-caught-exception-instance-in-python-2-and-3

In Python 3 the Exception object doesn’t stay around after the except block is over, whether or not you assign it to a variable name using the as syntax or not. The reason being performance. This means the exception must be assigned to a different name 
to be able to refer to it after the except clause. So you will need to take the extra step of assigning it to a variable name explicitly in the except block if you want to use it after the block is over, e.g.:

    try:
        oper_will_raise_type_error = 1 / 'a'
    except TypeError as e:
        my_error = e
    finally:
        print(2, 'finally', my_error)

If you don’t explicitly assign e to my_error here, but would attempt to print() it later on, e.g. in the finally block, it won’t work because of the default behavior that gets rid of that variable association.

'''

try: 
    oper_will_raise_type_error = 1 / 'a'
except TypeError as FE:
    # stand in for exception handling
    pass
finally: 
    exception_details = sys.exc_info()
    print(1, 'when using except <exception> as <alias>', 'the', 'value in finally', exception_details)


try: 
    oper_will_raise_type_error = 1 / 'a'
except TypeError:
    # stand in for exception handling
    pass
finally: 
    exception_details = sys.exc_info()
    print(2, 'when using except <exception> WITHOUT <alias>', 'the', 'value in finally', exception_details)

