class AccessClassName:
    '''
    A simple  class to demonstrate the use of the self.__class__.__name__ attribute to access the class name dynamically
    '''
    def __init__(self):
        '''AccessClassName Constructor to initialize the objet
        
        Input Values: None
        '''
        pass 
        
    def print_class_name(self):
        '''prints value of attribute self.__class__.__name__'''
        print(self.__class__.__name__)

o
print_class_name()        