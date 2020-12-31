'''
This module demonstrates that there isn't a special significance to the self word. 
Regardless of the name the first parameter to a method defenition is treated just as self is.
In the function estimate_fuel_effeciency the argument 'essence' is a standin for 'self'. 
However using any other name instead of self is DISCOURAGED as it leads to a lot of confusion.
'''
from typing import Optional, Union
class Car:
    def __init__(self, color: str, mileage: Union[int, float], 
                 uom_mileage: Optional[str] = "Miles", uom_fuel_qty: Optional[str] = "Gallon"):
        """Car Class Constructor to initialize the object.

        Input Arguments: color must be str, mileage can be str or int
                         uom_mileage is optional. must be str if specified. Default value is "Miles"
                         uom_fuel_qty is optional. must be str if specified. Default value is "Gallon"
        """        
        self.color = color
        self.mileage = mileage
        self.uom_mileage = uom_mileage
        self.uom_fuel_qty = uom_fuel_qty

    def __repr__(self):
        return '__repr__ for Car'

    def __str__(self):
        return '__str__ for Car'

    def estimate_fuel_effeciency(essence):
        print(essence.mileage)
        if essence.mileage > 5:
            print(f'{essence.mileage} {essence.uom_mileage} per {essence.uom_fuel_qty}! That is pretty good mileage!')
        else:
            print(f"{essence.mileage} {essence.uom_mileage} per {essence.uom_fuel_qty}. You can get better mileage than that")


car = Car("Yellow", 5)
car.estimate_fuel_effeciency()