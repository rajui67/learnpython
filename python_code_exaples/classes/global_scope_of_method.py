class FirstClass:
    ''' Demonstrates that the global scope of a method is the module (<filename>.py) and not the class. In essence this means that if 2 classes are definied within the same file
    then meothods of both classes have access to the  data members of each other'''

    a_variable = ""

    def __init__(self):
        ''' FirstClass Constructor to initialize the object
            
        Input Arguments: None.
        '''
        pass
    
    def __repr__(self):
        return f'__repr__ for {self.__class__.__name__}'

    def __str__(self):
        return f'__str__ for {self.__class__.__name__}'

    def set_a_variable(self):
        '''Function sets value of its class variable as well as a CLASS VARIABLE OF ANOTHER CLASS.'''
        a_variable = "1"
        another_variable = "1"



class SecondClass:

    another_variable = ""

    def __init__(self)
        '''SecondClass Constructor to initialize the object
        
        Input Arguments: None
        '''
        pass

    def __repr__(self):
        return f'__repr__ for {self.__class__.__name__}'

    def __str__(self):
        return f'__str__ for {self.__class__.__name__}'

    def set_another_variable(self):
        '''Function sets value of its class variable as well as a data member OF ANOTHER CLASS.'''
        a_variable = "2"
        another_variable = "2"


object1 = FirstClass()
object1.set_a_variable()
print('1', FirstClass.a_variable, SecondClass.another_variable)

object2 = SecondClass()
object2.set_another_variable()
print('2', FirstClass.a_variable, SecondClass.another_variable)
