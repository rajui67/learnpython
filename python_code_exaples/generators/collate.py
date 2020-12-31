'''This module demonstrates that a yield statement in a function makes the function a generator'''

from typing import Union, List, Tuple

def collate(*args):
    '''A generator function. 

    Args: 
        Each arg is an iterable. All args have the same number of elements. 

    Yields: 
        tuple(value of next element of iterable1, next element of iterable2, next element of iterable3, ...)
    
    Exceptions:
        If the first arg has more number of elements than any of the other arguments then iterating past the len(argument) of the argument that has the least number of elements will result in the error IndexError: list index out of range
 
    All elements of args[1], args[2] that fall beyond len(arg[0]) will be discarded.

    Example:

        array1 = [11, 12, 13]
        array2 = [21, 22, 23, 24, 25]
        array3 = [31, 32, 33] 
        generator = collate(array1, array2, array3, array4, array5)
        for value in generator:
            print(value)
        pass
    
    Will result in:
        (11, 21, 31)
        (12, 22, 32)
        (13, 23, 33)    
    '''
    
    total_number_of_arguments = len(args)
    total_iterations = len(args[0])
    for  iteration in range(0, total_iterations):
        collated_value = []
        for argument_number in range(0, total_number_of_arguments):
            collated_value.append(args[argument_number][iteration])
        yield tuple(collated_value)

if __name__ == "__main__":
    array1 = [11, 12, 13]
    array2 = [21, 22, 23, 24, 25]
    array3 = [31, 32, 33] 
    array4 = [41, 42, 43]
    array5 = (52, 53, 54)
    generator = collate(array1, array2, array3, array4, array5)
    for value in generator:
        print(value)
    pass