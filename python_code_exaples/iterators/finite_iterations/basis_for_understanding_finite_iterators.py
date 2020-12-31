'''
Every iterable has an iter(iterable) function which is a wrapper over iterable.__iter__(). 
iterable.__iter__() returns an iterator. An iterator is an object that may be iteratred over.
When such an object is iterated over, every iteration returns the next element of the iterable.  

Every iterable has an next(iterator) function which is a wrapper over iterator.__next__(). 
iterator.__next__() is the statement that produces the next iteration.
'''
string1 = 'abc'
iterator = iter(string1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) will raise StopIteration

list1 = ['la', 'lb', 'lc']
iterator = iter(list1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) will raise StopIteration

tuple1 = ('ta', 'tb', 'tc')
iterator = iter(tuple1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) will raise StopIteration

set1 = {'sa', 'sb', 'sc'}
iterator = iter(set1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) will raise StopIteration

dict1 = {'da': 'da1', 'db': 'db1', 'dc': 'dc1'}
iterator = iter(dict1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
