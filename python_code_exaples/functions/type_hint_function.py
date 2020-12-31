def printit(string: str) -> None:
    '''
    This  is an exaple of defining a function using python type hinting. Anyone seeing the function definition will know what 
    type  of parameters the function expects and what type of value the function returns.
    These types are not enforced by python. there are some external packages, e.g. mypy that make it possible to enforce static 
    typing in python.

    https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b
    https://docs.python.org/3/library/typing.html#module-typing
    https://docs.python.org/3/library/typing.html#typing.Union
    https://stackoverflow.com/questions/41356784/how-to-use-type-hints-in-python-3-6
    '''
    my_string = 'Ha'
    string += ' ' + my_string
    print(string)


my_string = 'Nonsense'
printit(my_string)
print(my_string)
