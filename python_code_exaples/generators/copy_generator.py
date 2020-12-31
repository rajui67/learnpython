'''Copying a generator does not work. Generates the following error
      File "<actual file na,e>", line <actual line #. in this case 14>, in <module>
        receptor = dispatch_table.get(cls)
    NameError: name 'dispatch_table' is not defined
'''

from copy import copy

base = [1, 2, 3]
generator = (element/2 for element in base if element % 2)
ga = getattr(generator, "__reduce_ex__", None)
cls = type(generator)
receptor = dispatch_table.get(cls)
generator1 = copy(generator)
