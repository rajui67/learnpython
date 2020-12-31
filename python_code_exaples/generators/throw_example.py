def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


infinite_sequence_generator = infinite_sequence()       
for counter in infinite_sequence_generator:
    print(counter)
    if counter == 10:
        infinite_sequence_generator.throw(ValueError, "Enough! Stop Iterating!")
        
