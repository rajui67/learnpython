'''
This is probably an exaple of how NOT to write code, but let us look at how this code snippet works.
The array1.reverse function is executed and array1 becomes the original array1 with elements in reverse order
The return value of array1.function is None. 
The conditional expression is evaluated using None (the returen value of array1.reverse) 
The condition evaluates to True (None is a Falsy and not of a Falsy is True) 
An annymous list [14, 13, 12] is created
The Anonymous list is printed 
NOTE that  array1 itself is reversed as it is required to evaluate the condition 
'''
array1 = [8, 9, 10, 11, 12, 13, 14]
print(f'{array1[:3] if not array1.reverse() else None}')

