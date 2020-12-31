'''
Demonstrates that generator and range take very little memory as each is lazy. 
Lists are created in memory at run time and the memory footrpint reflects.

generators may  have ANY value as their return value
generator elements are consumed when they are looped over.
generators cannot be accessed with subscripts

A range is a bounded range of NUMBERS
Range objects persist their values and can be iterated over multiple times.
Range objects can be accessed with subscripts

'''

import sys
def bounded_repeater(value: str, max_repeats: int) -> iter:
    for i in range(max_repeats):
        yield value + str(i)

def bounded_repeater1(max_repeats: int) -> iter:
     return range(max_repeats)

generator = bounded_repeater('Hello', 100000)
range_of_values =  bounded_repeater1(100000)
array = [i for i in  bounded_repeater('Hello', 100000)]

print(type(generator), type(range_of_values), type(array))
print(sys.getsizeof(generator), sys.getsizeof(range_of_values), sys.getsizeof(array))

generator = bounded_repeater('Hello',3)
range_of_values =  bounded_repeater1(3)

print('First loop through generator')
for i in generator:
    print(i)

print('Second loop through generator')
for i in generator:
    print(i)

print('First loop through range')
for r in range_of_values:
    print(r)

print('Second loop through range')
for r in range_of_values:
    print(r)

print (r := range_of_values[1] + 10)
# print (i := generator[1] + 10) # will result in TypeError: 'generator' object is not subscriptable