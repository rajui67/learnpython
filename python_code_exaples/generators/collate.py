'''This module defines the collate function'''

def collate(*args):
    '''A generator function yielding tuples until input is exhausted.
    
    >>> list(collate('ab', [11, 12, 13], [21, 22, 23, 24]))
    [('a', 11, 21), ('b', 12, 22), (None, 13, 23), (None, None, 24)]
    
    The collate object yields n tuples, where n is the number of elements of the largest iterable. The size of each tuple is equal to the number of arguments to collate(). The i-th element in every tuple comes from the i-th iterable argument to collate(). This continues until the largest argument is exhausted. Smaller arguments contribute None in lieu of their i-th element once they are exhausted.  

    Args: 
        Takes any nuqmber of arguments. Each arg is an iterable. 
    '''
    
    total_number_of_arguments = len(args)
    total_iterations = 0
    for itble in args:
        if len(itble) > total_iterations:
            total_iterations = len(itble)

    for  iteration in range(0, total_iterations):
        collated_value = []
        for argument_number in range(0, total_number_of_arguments):
            collated_value.append(args[argument_number][iteration] if len(args[argument_number]) > iteration else None)
        yield tuple(collated_value)

if __name__ == "__main__":
    array1 = [11, 12, 13]
    array2 = [21, 22, 23, 24, 25, 26, 27]
    array3 = [31, 32, 33] 
    array4 = [41, 42, 43]
    array5 = [52, 53, 54]
    collater = collate(array1, array2, array3, array4, array5)
    for value in collater:
        print(value)
