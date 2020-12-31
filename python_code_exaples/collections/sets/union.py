set1 = {1, 2, 3}
set2 = {1, 5}
print(set1 | set2)
print(set1.union(set2))
print(set2 | set1)
print(set2.union(set1))
# up until this point set1 and set2 remain unchanged. The operators and function return a new set 
print(set1, set2)

set1 = {1,1,2,2,3}
set2 = {1,5}
# |= a shortcout operator. Essentially, set1 |= set2 works thus so:
# 1. executes set1 | set2 which creates a new anonymous set. 
# 2. set1 = new set #set1 is modified such that its object-refence is the same as set2's object reference
set1 |= set2 
print('short cut operator |=', set1)
#print(set1 |= set2) This generates an error. An assignment or shortcut operator cannot be used 'inline'. 


# The assignment expression := can be used to assign a value . TUt works thus so:
# 1. Executes the  set1 | set2 operation whcih creates a new set.
# 2. set1 = new set #set1 is modified such that its object-refence is the same as set2's object reference 
# set1 is printed 
set1 = {1,1,2,2,3}
set2 = {1,5}
print('Assingnment expression :=', set1 := set1 | set2) 
