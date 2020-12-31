set1 = {1,1,2,2,3}
set2 = {1,7,23}
set1.update(set2) # updates set1 with the values from set2. The update function itself returns None. so something like print(set1.update(set2)) will UPDATE set1 but return None
print(set1, set2)