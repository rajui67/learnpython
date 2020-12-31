def bounded_sequence(upper_bound: int) -> int:
    counter = 0
    while True:
        value_received = yield counter
        if value_received is not None:
            counter += value_received
        if counter >= upper_bound:
            break
        counter += 1

bs = bounded_sequence(12)

# Will work as a generator expression never raises a StopIteration excpetion itself
for sequence_number in bs:
    pass


bs = bounded_sequence(12)
#will generate a StopIteration exception
for sequence_number in bs:
    bs.send(8) 

#This will exit the loop immediately. The first call to next will return 0. 0 is assigned to bounded_sequence_generator and then the program checks the condition
# for the while loop. 0 is  a falsy and hence the condition evaluates to false and never executes
try:
    while (sequence_number := next(bs)):
        pass
except StopIteration as SI:
    pass

# This will generate an error because the 13th iteration will raise the StopIteration exception
while True:
    bounded_sequence_generator = next(bs)
    pass
