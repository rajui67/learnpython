'''
This script demonstrates that assigning one list to another makes both those lists refer to the same object. This is how it works for tuples as well as sets. Tuples are immutable; therefore no practical impact.

Each of the elements of the array_of_arrays list is a reference to the base_array list. Any changes to the elements of base_array, or, any of the sub-lists (anonymous lists that are, in turn, elements of the array_of_arrays list )
is reflected immediately on base_array and all sub-lists.  array_of_arrays[0], array_of_arrays[1], array_of_arrays[2], and base_array all reference the same object.

'''
import os

os.system('clear')

base_array = []
array_of_arrays = [base_array for i in range(3)]  

base_array.append(16)
array_of_arrays[0].append(17)
array_of_arrays[1].append(18)
array_of_arrays[2].append(19)
print('Value of  "base_array"  ', base_array) 
print('Value of  "array_of_arrays"  ', array_of_arrays) 

''' With this assignment, the 2nd element of array_of_arrays and base_array dont refernce the same object any more. The 2nd element of array_of_arrays references a new, anonymous, list type; object.''' 
array_of_arrays[1] = ['a', 'b', 'c']
print('Value of  "base_array"  ', base_array)
print('Value of  "array_of_arrays"  ', array_of_arrays) 
