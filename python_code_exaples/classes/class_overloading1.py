import os

class Animal:
    '''
    In Python constructors are overloaded by using default values for parameters. The constructor of this class expects two parameters
    name is mandatory and is_a_type_of is not. If a is_a_type_of isnt supplied to the constructor when creating an instance, the objexct will be created 
    with the value [No is_a_type_of] assigned to the is_a_type_of object attribute.
    '''
    
    def __init__(self, name: str, is_a_type_of: str=""):
        """Animal Class Constructor to initialize the object.

        Input Arguments: name must be str, 
                         is_a_type_of is optional. must be str if specified.  Default value is "" 
        """
        self.name = name
        if is_a_type_of != "" :
           self.is_a_type_of = is_a_type_of
    
    def print_me(self):
        print([name for name in dir(self) if not (name.startswith('__') and name.endswith('__'))])

os.system("clear")
s1 = Animal(name = 'Deer')
s1.print_me()
s2 = Animal("Goose", "Bird")
s2.print_me()
