from repeater_plus_iterator import Repeater, RepeatIterator

repeater = Repeater('abc')
iterator = repeater.__iter__()

#same functionaliy
counter = 0
while True:
    iteration = iterator.__next__()
    print(iteration)
    counter += 1
    if counter == 3:
        break

print(), print()
#same functionaliy
another_iterator = iter(repeater)
print(iteration := next(iterator))
print(iteration := next(iterator))
print(iteration := next(iterator))