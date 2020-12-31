def main():

    demo  = Demo(1)
    demo1 = Demo(2)
    pass
    Demo.some_data_member = 10
    pass    

class Demo():
    ''' A simple demonstration that class level variables are shared by every instance of the class and the moudule
    '''
    some_data_member = "I am a class level data member"

    
    def __init__(self, some_value):
        """Demo Class Constructor to initialize the object.
        Sets the value of class variable some_data_member to some_value
        Inputs: some_valeue type Any
        
        Returns: None

        Input Arguments: None
        """
        Demo.some_data_member =  some_value

if __name__ = "__main__":
    main()