from repeater_plus_iterator import Repeater, RepeatIterator

# This is the same as
# next(repeater) TypeError: 'Repeater' object is not a generator
repeater = Repeater('abc')
counter = 0
for each in repeater:
    print(each)
    counter += 1
    if counter == 3:
        break



