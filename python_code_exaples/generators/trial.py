from copy import copy
from random import random

class Repeater():
    
    def __init__(self, max_repetitions):
        self.max_repetitions = max_repetitions
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repetitions :
            raise StopIteration
        else:
            self.count += 1
            return random()
  


repeater = Repeater(2)
iterator = iter(repeater)
iterator1 = copy(iterator) 
for value in iterator:
    print(value)

base = [1, 2, 3]
generator = (element/2 for element in base if element % 2)
ga = getattr(generator, "__reduce_ex__", None)
pass
generator1 = copy(generator)