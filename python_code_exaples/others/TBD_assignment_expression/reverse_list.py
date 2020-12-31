def reverse_list(array: list):
    ''' Simulates the built in reverse function'''

    '''Arrays are passed by reference. Therefore, if you do not want to change the original values of an array, it is necessary to make a copy of the array 
    and make any modifications to the cpy'''
    private_array = [*array] # both statements make a shallow copy of the array
    #private_array = array.copy()

    for counter in range(0, len(private_array)):
        private_array.insert(counter,private_array[-1])
        private_array.pop(-1)
    return private_array

