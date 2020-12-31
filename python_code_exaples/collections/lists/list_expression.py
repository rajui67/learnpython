import os
import sys

os.system('clear')

# list comprehension or expression 
array = [a for a in range(10000)]

# generator comprehension or expression 
list_generator =  (g for g in range(10000))
print(type(array), type(list_generator))

print('array', sys.getsizeof(array))
print('list_array', sys.getsizeof(list_generator))


