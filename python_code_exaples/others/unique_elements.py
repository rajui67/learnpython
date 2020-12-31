from typing import Union, List, Tuple

def all_unique(collection: Union[List, Tuple]) -> bool:
    return len(collection) == len(set(collection))


x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True

a = (1,1,2,2,3,2,3,4,5,6)
b = (1,2,3,4,5)
all_unique(a) # False
all_unique(b) # True