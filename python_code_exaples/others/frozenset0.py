'''
https://www.geeksforgeeks.org/frozenset-in-python/
'''

listu = [10, 20, 30, 40, 50, 60]
tup = ("a", "b", "c", "dictu") #tuples are immutable
setu = {"This", "This", "That", "That", "Those"}
dictu = { "key1": "value1", "key2": "value2"}

listu[0] = 18
listu.append(1000)

'''
setu[0] = setu[0].upper()
set data structure is an unordered collection of unique elements. It doesn't support operations like indexing or slicing etc. 
However, values may be added to a set
'''
setu.add("These")

dictu["key3"] = "value3"
#print(listu, tup, setu, dictu)

listf = frozenset(listu)
setf = frozenset(setu)
dictf = frozenset(dictu)
#print(f'frozenset [listf] {listf} of list [listu] {listu}')
#print(f'frozenset [listf] {setf} of list [listu] {setu}')
#print(f'frozenset [dictf] {dictf} of dict [dictu] {dictu}')

for item in listf: 
    print(item)

for item in setf:
    print(item)

for item in dictf:
    print(item, dictu[item])