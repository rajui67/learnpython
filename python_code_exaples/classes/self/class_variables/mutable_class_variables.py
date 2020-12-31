'''
This module illustrates the behavior of mutable class level data members vis-a-vis the self object.

When an element of a  class level mutable data member is modified with notation used to modify an element of a mutable instance data member BEFORE the instance data member is initialized,
It is the element of the class level data member that is changed.

Once the instance data member is initialized, the instance data member is an independent object (independent of the class level object of the same name)

Elements of instance level data members can modified using one of these methods:

    invoking a method which within its body modifies the element thus so:
         "self.<data member>[<key>] = value" (Note: __init__ runs as part of the object instantiation process and need not be explicitly invoked)
         "<instance>.<data member>[<key>] = value" from the enclosing scope of the instance

Elements of instance level data members may be initialized through one of these methods:

    invoking a method which within its body modifies the element thus so:
      "self.<data member> = value" (See note on __init__above)

    From the enclosing body encapsulating the instance, thus so:
        <instance> = <class>() # creates the instance
        <instance>.<data member>[<key>] = value
'''



class Mutable:
    '''Models a class with mutable class level data members'''

    some_array_member = [1, 2]
    another_array_member = [3, 4]

    def __init__(self):
        """Mutable Class Constructor to initialize the object.
        Modifies element values using notation used for instance level data members

        Input Arguments: None
        """
        self.some_array_member[0] = 11
        self.some_array_member[1] = 21

def main():
    mutable = Mutable()
    mutable.another_array_member= [31, 41]
    pass

if __name__ == "__main__":
    main()