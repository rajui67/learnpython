'''
NOTE: When a generator.send is used in the body of a for loop iterating over the generator, It more often than not will generate
a StopIteration error. It is just plain luck if it doesn't 
'''

#Defined as module variables just so that they can be used in debugging
# works in tandem with global statement in function body
sequence_number, counter, value_received, some_var = -1, -1, -1, -1


def bounded_sequence(upper_bound: int) -> int:
    ''' Generator function to generate a finite number of numbers 

    Inputs: upper_bound must be int
    Returns None
    '''
    # global for debugging purposes
    global sequence_number, counter, value_received
    counter = 0
    while True:
        value_received = yield counter
        if value_received is not None:
            counter += value_received
        if counter > upper_bound:
            break
        counter += 1


bounded_sequence_generator = bounded_sequence(9)
for sequence_number in bounded_sequence_generator:
    somevar = bounded_sequence_generator.send(8)
