import mutable_class_variables

class AlsoMutable(mutable_class_variables.Mutable):
    '''Models a subclass'''
    
    def __init__(self):
        """Initialize subclaa
        """
        self.some_array_member[0] = 111
        self.some_array_member[1] = 211


also_mutable = AlsoMutable()
also_mutable.another_array_member = [311, 411]
pass