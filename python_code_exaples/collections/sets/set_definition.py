
setu = {"This", "This", "That", "That", "Those"}

print('This will not work on a set: set[0] = "Value"\n'
      '''set data structure is an unordered collection of unique elements. It doesn't support operations like indexing or slicing etc.\n'''
      'However, values may be added to a set and it my be iterated over using the for loop')

setu.add("These")


setf = frozenset(setu)
print(f'frozenset [listf] {setf} of list [listu] {setu}')

for item in setf:
    print(item)

