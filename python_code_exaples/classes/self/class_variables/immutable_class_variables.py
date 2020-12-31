'''
This module illustrates the behavior of immutable class level data members vis-a-vis the self object.

When a class level data member is accessed with notation used to access an instance data member BEFORE the instance data member is initialized. The instance data member is a reference to the class data member. 

Once the instance data member is initialized, the instance data member is an independent object (independent of the class level object of the same name) 

Accessing instance data members can be through one of these methods:

    self.<data member> within class methods
    instance.<method>() which returns self.<data member>
    <instance>.<data_member> from the enclosing scope of the instance      
    
Instance variable may be initialized through one of these methods:

    self.<data_member> =  <some value> within the constructor method __init__
    self.<data_member> =  <some value> wihtin any of the objects method

    (NOTE: The difference between the two is when the data members are initialized. 
    The constructor instantiates the object and therefore the instance is created with instance varibale already initialized.
    Other methods execute only when invoked. If the method is never invoked, the data_member is never initialized) 

    From the enclosing body of the instance thus so: 
        <instance> = <class>() # creates the instance
        <instance>.<data member> = <some value>
'''


class Immutable:
    '''Models a class with immutable class level data members'''
    some_data_member = "I am a class level data member"
    another_data_member = 'I am another class level data member'
    yet_another_data_member = 'I am yet another class level data member'

    def __init__(self):
        """Immutable Class Constructor to initialize the object.
        self.some_data_member is initialized
        self.another_data_member and yet_another_data_member are NOT

        Input Arguments: None
        """
        self.some_data_member = "I was initialized in __init__ (the constructor)." + "\n" + \
            "From this point I am an instance level variable."

    def set_another_data_member(self):
        self.another_data_member = "I was initialized in method set_another_data_member." + "\n" + \
            "From this point I am just another instance leve data member"


immutable = Immutable()
immutable.set_another_data_member()
immutable.yet_another_data_member = 'I was initialized in the main body of the module.\n'
