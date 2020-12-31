'''
Extend uderstanding gained from basis_for_understanding_finite_iterators.py
'''


class BoundedRepeater():
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater('abc', 3)
iterator = iter(repeater)
while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break

# At this point, the iterator has been exhausted of all its values.
# The while clause has iterated over the iterator and consumed all its
repeater = BoundedRepeater('abc', 3)
# for value in repeater: is a wrapper over the above while bloc starting from
# iterator = ... to the break statment
# NOTE: the for clause creates the iterator object and then iterates over it
for value in repeater:
    print(value)
