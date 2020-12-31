from typing import Optional, Union

class Car:
    def __init__(self, color: str, mileage: Union[int, float], uom_mileage: Optional[str] = 'Miles', 
                 uom_fuel_qty: Optional[str] = "Gallon"):
        """Car Class Constructor to initialize the object

        Input Arguments: color must be str
                         mileage must be int or float. 
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

car = Car("Red", 100)        

'''Enter the following in interactive window and run it to see values returned
    Check the values of str(car), print(car), repr(car), car'''
