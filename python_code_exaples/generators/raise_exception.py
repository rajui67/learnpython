''' Shows that generator functions are no different than other functions when it comes to exceptions.
    Any exception raised within the function is propagated to its enclosing block.
    Notice that the message generated is unique when the exception raised within the generator function is StopIteration 
'''

#    This will fail with the message:
#     File <actual file name>, line <actual line number >, in bounded_sequence
#        raise ValueError 
#     ValueError 
#      A similar error would be generated for all other exceptions raise

def bounded_sequence(upper_bound: int) -> int:
    counter = 0
    while True:
        value_received = yield counter
        if value_received is not None:
            counter += value_received
        if counter > upper_bound:
            raise ValueError 
        counter += 1

bs = bounded_sequence(3)

for sequence_number in bs:
    print(sequence_number)


#    This will fail with the message:
#     File <actual file name>, line <actual line number >, in bounded_sequence
#       for sequence_number in bs:
#     RuntimeError: generator raised StopIteration
def bounded_sequence(upper_bound: int) -> int:
    counter = 0
    while True:
        value_received = yield counter
        if value_received is not None:
            counter += value_received
        if counter > upper_bound:
            raise StopIteration 
            break
        counter += 1

bs = bounded_sequence(3)

for sequence_number in bs:
    print(sequence_number)

