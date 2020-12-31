class Demo:
    '''
    Self is just another object, freely available to all its meothods. Therefore, It is not just __init__, any other  method within the object can add attributes to it.
    This means that if a value is ASSIGNED to a non existing variable in a non __init__ method A NEW DATA MEMBER IS CREATED. 
    (Assume that you typed in var11 by mistake. Your intention was to type var1)
    '''

    def __init__(self):
        """Demo Class Constructor to initialize the object.

        Input Arguments: None
        """
        self.var1 = 'Initialized by Constructor'

    def add_to_me(self):

        # The below statement would have raised the AttributeError exception with the error message 'Demo' object has no attribute 'var11'
        #self.var11 += 'Added by Function add_to_me'

        # This statement works as it creates a new data member
        self.var11 = 'Added by Function add_to_me'

        # This statement works as it opearates on a data member created in the constructor
        self.var1 += ' += operation on an existing object instance string attribute works just fine'

    def print_me(self):
        print([name for name in dir(self) if not (
            name.startswith('__') and name.endswith('__'))])


os.system("clear")
s1 = Demo()
s1.add_to_me()
s1.print_me()

s2 = Demo()
s2.print_me()
