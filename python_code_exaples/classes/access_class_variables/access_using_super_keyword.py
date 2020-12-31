from aqua import Aqua

class Turtle(Aqua):
    ''' This class denomstrates one way of accessing private class variables of the parent class.
        The Aqua class has a variable called __waterbodies. Python mangles this name to _Aqua__wateerbodies. 
        This class accesses the mangled name using the super keyword

        NOTE: Just because we can do something doesn't mean we should do it.
              Accessing parent members this way harcodes the parent class and should be avoided.
    '''
    
    def __init__(self, waterbody):
        """Turtle Class Constructor to initialize the object.

        Input Arguments: waterbody must be str
        """        
        pass
        if waterbody in super()._Aqua__waterbodies:
            self.habitat = {'waterbody': waterbody}

loggerhead = Turtle('Pond')
print (loggerhead.habitat['waterbody'])
print(loggerhead._Aqua__waterbodies)
