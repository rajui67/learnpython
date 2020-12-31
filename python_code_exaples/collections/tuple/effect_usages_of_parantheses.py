# NOTE: this does not generate a tuple it generates a generator object
gen = (value for value in range(5))
# for gen_value in gen:
#     print(gen_value)

# generates a tuple
tup1 = tuple(range(5))

# generates a tuple
tup2 = tuple((value for value in range(5)))

# generates a tuple. each element of the tuple is the corresponding element of the list (comprehension).
# In this case each element of the list is itself a list. Therefore each element of the tuple is a list 
array = [[1,2], [3,4], [5,6]]
tup3 = tuple((element for element in array))

# tup4 is a copy of intermediate_tuple. both tuples will reference the same underlying object.
# has the same effect as  tup4 = intermediate_tuple
intermediate_tuple = 1, 2, 3, 4, 5
tup4 = tuple(intermediate_tuple)

# using the brackets notation to specify a tuple. 
# tup5 is a copy of another_intermediate_tuple.  both tuples will reference the same underlying object.
# has the same effect as  tup5 = another_intermediate_tuple
another_intermediate_tuple = (1, 2, 3, 4, 5)
tup5 = tuple(intermediate_tuple)
pass