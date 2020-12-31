from aqua import Aqua 

class Fish(Aqua):
    ''' This class denomstrates one way of accessing private class variables of the parent class.
        The class Aqua has a method  get_waterbodies. Methods in the class access the method by invoking  get_waterbodies
    '''
    def __init__(self, waterbody: str):
        """Fish Class Constructor to initialize the object.

        Input Arguments: waterbody must be str
        """        
        pass
        if waterbody in super().get_waterbodies():
            self.habitat = {'waterbody': waterbody}
        else:
            self.habitat = {'waterbody': 'Invalid'}

guppy = Fish('Puddle')
print(guppy.habitat['waterbody'])


