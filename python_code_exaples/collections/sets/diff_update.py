s = {1,1,2,2,3} # This will create as set s {1, 2, 3} as each element of the set is unique (by definition of what a set is in the pyhton language)
s1 = {1,5}
'''this call {s.difference_update(s1)}' from within a f-string will return: None
      This is because:
      The embedded function difference_update runs, and the value of the set s will change to  {2, 3}. 
      The function difference_update returns tNone and that is the value that is printed
'''
print(f'{s.difference_update(s1)}') 
print(s)
