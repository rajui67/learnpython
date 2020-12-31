from aqua import Aqua

class Frog(Aqua):
    ''' This class denomstrates one way of accessing private class variables of the parent class.
        The Aqua class has a variable called __waterbodies. Python mangles this name to _Aqua__wateerbodies. 
        This class accesses the mangled name using <classname>.<variablename> .

        NOTE: Just because we can do something doesn't mean we should do it.
              Accessing parent members this way harcodes the parent class and should be avoided.
    '''    
    
    def __init__(self, waterbody):
        """Frog Class Constructor to initialize the object.

        Input Arguments: waterbody must be str
        """        
        pass
        if waterbody in Aqua._Aqua__waterbodies:
            self.habitat = {'waterbody': waterbody}

african_dwarf_frog = Frog('Pond')
print (african_dwarf_frog.habitat['waterbody'])

