class Fish():
    def __init__(self):
        ''' Fish Constructor to initalize the object
        
        Input Arguments: None
        '''
        self.name = self.__class__.__name__
        self.habitat = 'Water'
        # thermoregulation -  how the body regulates its temperature 
        # Homeothermic - maintains a constant internal body temperature
        self.thermoregulation = 'Homeothermic' 
        self.respiration = 'Gills'

#Empty class
class Chichlid(Fish):
        pass

guppy = Chichlid()
print(guppy.name, guppy.thermoregulation, guppy.respiration)