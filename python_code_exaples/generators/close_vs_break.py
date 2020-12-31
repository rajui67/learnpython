'''
Demonstrate the difference in behavior between break and close to exit out of a for loop looping over a generator
'''
def infinite_sequence():
    ''' generator for infinite sequence
    '''
    num = 0
    while True:
        yield num
        num += 1


infinite_sequence_generator = infinite_sequence()       
for counter in infinite_sequence_generator:
    print(counter)
    if counter == 10:
        break
# This will generate the next number. CLEARLY not the intention, in most cases, when breaking out of a generator for loop  
counter = next(infinite_sequence_generator)    
print(counter)        

infinite_sequence_generator = infinite_sequence()       
for counter in infinite_sequence_generator:
    print(counter)
    if counter == 10:
        infinite_sequence_generator.close()
# This will generate the StopIteration exception. In most cases the intention when breaking out of a generator for loop is that
# that you cannot successfully run next() or .send on that generator
counter = next(infinite_sequence_generator)    
print(counter)        
