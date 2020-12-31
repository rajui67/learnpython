
'''
Examples of issues that arise when using send() on a generator function (or generator expresssion) . 

Every iteration over a  generator (or generator expression) is like calling next() on the generator object instance. 

Which means:

1. The first call will enter the loop and yield the value of product, suspend itself, and return control to the calling block. 
2. Every other call will activate the generator function from the point where it was suspended.
3. The first action it does is to take in the value that was passed into the generator function from the outside environment:
    next(generator) sends None.
    generator.send(<value>) the <value>.

Here is an example where forgetting this could trip one up.The code itself is a piece of silly code, 
(As of this time, I cannot think of a situation where I would use .send() to interact with such a function) 
However, it helps illustrate the point.

NOTE: The for loop in this program generates an infinite loop
Each iteration of the generator expression (the for loop over a generator) is like starting the iteration with a call to the next(multiplier_sequence_generator) function
1. The begining of the 1st iteration  invokes a next(multiplier_sequence_generator) and sets the value of it_val to 3
2. The .send method is called and sets the value of it_val to 6.  # "multiplier_sequence_generator.send(none) is equal to next(multiplier_sequence_generator)" 
   if statement evaluates to false
3. The beginning of the 2nd iteration invokes a next(multiplier_sequence_generator) sets the value of it_val to 9
4. The .send method is called and sets the value of it_val to 12 
   At this point it_val is already greater than 9 and the if statement evaluates to false 
The program will never exit this loop as it_val will never have the value 9

'''
import os
os.system('clear')


def multiplier_sequence(multiplicand: int):
    '''
        A generator that yields multiples of a given multiplicand in an INFINITE loop
    '''
    multiplier = 1
    while True:
        product = multiplier * multiplicand
        value_received = (yield product)
        if value_received is not None:
            multiplier = value_received
        multiplier += 1


multiplier_sequence_generator = multiplier_sequence(3)
for it_val in multiplier_sequence_generator:
    print('The value returned by the send method =', it_val := multiplier_sequence_generator.send(3))
    if it_val == 9:
        break

    # to break the infinte loop
    # if it_val == 12:
    #     break
