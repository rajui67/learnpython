'''
BE CAREFUL when modifying varibales or object instances within an F-strings when those variables are also otherwise referenced in the F-string. See the difference in the output of the two print statements
In both cases the eventual valule of base_set is {2, 3} but:
 the first prints "None {2, 3}". and the second  "{1, 2, 3} None"
'''
base_set = {1, 2, 3} 
the_other_set = {1, 5}


print(f'{base_set.difference_update(the_other_set)} {base_set}') 
#print(base_set)

base_set = {1, 2, 3} 
the_other_set = {1, 5}


print(f'{base_set} {base_set.difference_update(the_other_set)} ') 
#print(base_set)
