from typing import Union

class Rectangle:
    def __init__(self, length: Union[int, float], width: Union[int, float], **kwargs):
        '''Rectangle Constructor to intialize the object
        
        Input Values: length must be int or float
                      width must be int or float
                      kwargs must be <how do I annotate kwargs?> 
        '''
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length: Union[int, float], **kwargs):
        '''Square Class Constructor to init object
           
           Input Values: length must be int or float, 
                          kwargs must be <how do I annotate kwargs?>. 
        '''
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length



class Triangle:
    def __init__(self, base: Union[int, float], height: Union[int, float], **kwargs):
        '''Triangle Class Constructor to init object
           
           Input Values: base must be int or float,  height must be int or float
                         kwargs must be <how do I annotate kwargs?>. 
        '''
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base: Union[int, float], slant_height: Union[int, float], **kwargs):
        '''RightPyramid Class Constructor to init object
           
           Input Values: base must be int or float,  slant_height must be int or float
                         kwargs must be <how do I annotate kwargs?>. 
        '''
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area