'''
I deliberately omitted the parantheses after what_is_my_class_name in the statement 
var = apple.what_is_my_class_name 
'''

class Fruit:
    """A simple Fruit class"""

    def __init__(self, color: str, smell: str):
        """Fruit Class Constructor to initialize a fruit object with its color and smell atrributes

        Input Arguments: color must be str, smell must be str
        """        
        self.color = color
        self.smell = smell
     
    # def __repr__(self):
    #     return '!whatever value is returned by __repr__'

    def what_is_my_class_name(self):
       return self.__class__.__name__


apple = Fruit("Golden Yellow", "Good")

#deliberately omitted the parantheses. var holds a reference to method what_is_my_class_name  
var = apple.what_is_my_class_name 

# returns <class 'method'>. object is an instance of method type object
print(type(var)) 

# var behaves like a function. can be invoked 
print(var()) 

# since var is a variable it can be assigned any value including a lambda function
var = lambda  : 'LAMBDA'

# var now returns 'LAMBDA'
print(var())

# apple.what_is_my_class_name() still returns 'Fruit'
print(apple.what_is_my_class_name())