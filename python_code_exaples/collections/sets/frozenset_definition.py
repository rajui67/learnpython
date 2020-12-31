setf = frozenset({"This", "This", "That", "That", "Those"})
print(f'{type(setf)} frozenset [listf] {setf}')
setf.add('These') # will generate error

for item in setf:
    print(item)

