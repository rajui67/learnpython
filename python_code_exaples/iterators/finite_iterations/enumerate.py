'''
Extend understaning gained from basis_for_understanding_finite_iterators.py and bounded_repeater.py to write custom version fo enumerate
'''


class Enumerate():
     '''Custom version of enumerate
     '''
    def __init__(self, iterable):
        ''' initialize the Enumerate object
        '''
        # This is essential. This is what enables the next() statment in the __next__ function  
        self.iterator = iter(iterable)
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return (self.count, next(self.iterator))


if __name__ == "__main__":
    string1 = 'abc'
    list1 = ['la', 'lb', 'lc']
    tuple1 = ('ta', 'tb', 'tc')
    set1 = {'sa', 'sb', 'sc'}
    dict1 = {'key0': 'db0', 'key1': 'db1', 'key3': 'dc1'}

    print("\n==\n", type(string1), end="\n==\n")
    for number, value in Enumerate(string1):
        print(number, value)

    print("\n==\n", type(list1), end="\n==\n")
    for number, value in Enumerate(list1):
        print(number, value)

    print("\n==\n", type(tuple1), end="\n==\n")
    for number, value in Enumerate(tuple1):
        print(number, value)

    print("\n==\n", type(set1), end="\n==\n")
    for number, value in Enumerate(string1):
        print(number, value)

    print("\n==\n", type(dict1), end="\n==\n")
    for number, value in Enumerate(dict1):
        print(number, value)

    print("\n==\n", type(dict1.items()), end="\n==\n")
    for number, value in Enumerate(dict1.items()):
        print(number, value)

    print("\n==\n", type(dict1.values()), end="\n==\n")
    for number, value in Enumerate(dict1.values()):
        print(number, value)
