import os
os.system('clear')

'''
Shows the impact of multiplaction on tuples
'''

base_tuple = (1,2,3)
tuple1 =  base_tuple * 3  # replicates the values of the elements of the tuple base_tuple 3 times and populates the values into the NEW tuple tuple1. 3 * null is null not 3 nulls.
tuple2 =  (base_tuple, ) * 3 # Creates a new tuple tuple2. Creates 3 elements in tuple2. Each element of tuple2 will  reference the same object that base_tuple does
tuple3 =  (*base_tuple, ) * 3 # unpacks each of the elements of base_tuple. replicates the values of the elements of the tuple base_tuple 3 times and populates the values into the NEW tuple tuple3. 

#output is 'base_tuple  (0, -10) tuple1  (0, -10, 0, -10, 0, -10) tuple2  ( (0, -10),  (0, -10),  (0, -10)) tuple3  (0, -10, 0, -10, 0, -10)'
print('base_tuple', base_tuple, 'tuple1', tuple1, 'tuple2', tuple2, 'tuple3', tuple3) 

