# In the context of this progaram, A generator is like generating a list. 
# The difference is that a list is created at the instant that it is defined.
# A generator returns each element of the list when the generator is operated on
base = [1, 2, 3]
generator = (element * 200 for element in base if element % 2)
while True:
    try:
        value = next(generator)
        print(value)
    except StopIteration:
        break 