def reverse_array(array: list):

   ''' Simulates the built in reverse function.  Arrays are passed by reference.'''

   for counter in range(0, len(array)):
        array.insert(counter,array[-1])
        array.pop(-1)
   return array


array1 = [1, 2, 3, 4, 5, 6, 7]  
print(array1, reverse_array(array1))

  
#print(array2 := [8, 9, 10, 11, 12, 13, 14] , f'{array2.reverse()}')

