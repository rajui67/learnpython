import os

class Demo:
    '''
    Note: instead of Demo.demo_of_what, the class variable demo_of_what could have been referenced as self.demo_of_what. 
    Both <Class Name>.<class attibute> as well as self.<class attribute> work.
    Please avoid this as soon as an instance data member by the same name is cretead self. refers to the instance data member and <class>. to the class data member  
    '''
    demo_of_what = "Class Variable"

    def __init__(self, name: str):
        ''' Demo class constructor to initialize the object
           
        Input Arguments: name must be str
        '''
        self.my_name = name

    def print_me(self):
        print((f'Value "when invoked with: self. [{self.demo_of_what}]" and also "when invoked with: <class>. [{Demo.demo_of_what}]"'))

os.system("clear")
s2 = Demo("Instance variable")
s2.print_me()

Demo.demo_of_what = 'Changed value of class variable'
s2.print_me()

s2.demo_of_what = 'Value of instance variable'
s2.print_me()