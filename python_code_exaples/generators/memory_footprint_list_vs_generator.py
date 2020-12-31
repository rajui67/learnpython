'''
Demonstrate the difference in size between a generator and an iterable
'''
import sys
base = {value:value for value in range(1,100000)}
# base = tuple(value for value in range(1,100000))
# base = {value for value in range(1,100000)}
# base = [value] for value in range(1,100000)]
new_base = [element * 200 for element in base if element % 2]
generator = (element * 200 for element in base if element % 2)
print (f'memory footprint of list [base] = {sys.getsizeof(base)}')
print (f'memory footprint of list [new_base] = {sys.getsizeof(new_base)}')
print (f'memory footprint of generator [generator] = {sys.getsizeof(generator)}')
