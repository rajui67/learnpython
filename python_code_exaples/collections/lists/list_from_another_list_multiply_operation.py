import os

os.system('clear')

'''
Shows the impact of multiplaction on lists
'''

base_array = []

# replicates the values of the elements of the list base_array 3 times and populates the values into the NEW list array1. 3 * null is null not 3 nulls.
array1 =  base_array * 3  

 # Creates a new list array2. Creates 3 elements in array2. Each element of array2 will  reference the same object that base_array does    
array2 = [base_array] * 3

# unpacks each of the elements of base_array. replicates the values of the elements of the list base_array 3 times and populates the values into the NEW #list array3. 3 * null is null not 3 nulls.
array3 = [*base_array] * 3 
base_array.append(-1)
base_array.append(-2)

# output is 'base_array = [-1, -2]; array1 = []; array2 = [[-1, -2], [-1, -2], [-1, -2]]; array3 = []'
print(f'base_array = {base_array}', f'array1 = {array1}', f'array2 = {array2}', f'array3 = {array3}', sep='; ') 

# just another example of all of the above
base_array = [0]
base_array.append(-10)
array1 =  base_array * 3  
array2 = [base_array] * 3
array3 = [*base_array] * 3


# output is 'base_array = [-1, -2, -10]; array1 = [-1, -2, -10, -1, -2, -10, -1, -2, -10]; 
# array2 = [[-1, -2, -10], [-1, -2, -10], [-1, -2, -10]]; array3 = [-1, -2, -10, -1, -2, -10, -1, -2, -10]'
print(f'base_array = {base_array}', f'array1 = {array1}', f'array2 = {array2}', f'array3 = {array3}', sep='; ')

