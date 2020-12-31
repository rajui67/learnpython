from all_decorators import this_decorates_that
'''
Shows two ways of decorating a function. way 1 and way 2. way 2 is syntactic sugar - a wrapper over way 1
'''


# way 1
def example1():
    print("Example 1")

example1 = this_decorates_that(example1) # this is the actual decoration

# way 2
@this_decorates_that
def example2():
    print("Example 2")

# Functions already decorated. This is just executing them. 
example1()
example2()