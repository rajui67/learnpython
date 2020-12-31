def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


for counter in infinite_sequence():
    print(counter)
    if counter == 10:
        break

infinite_sequence_generator = infinite_sequence()       
for counter in infinite_sequence_generator:
    print(counter)
    if counter == 10:
        break
        