'''
What is happening here?
The dict (kw) is built with key values equal to the argument names of the other classes in the class hierarchy
The constructor of each class calls the constructor of its immediate parent class, passing **kwargs as the parameter value.
Each contructor pops and consumes all those elements of  the kwargs dict whose key values are equal to the arguments  of the constructor
'''
from typing import Any

class Y:
    def __init__(self, **kwargs):
        ''' Y Class Constructor to initialize the object
        
        Input Values: kwargs ...
        '''
        super().__init__(**kwargs)
        print(5, kwargs)

class Z(Y):
    def __init__(self, value1: Any, **kwargs):
        '''Z Class Constructor to initialize the object
        
        Input Values: value1 may be of any type
                      kwargs ...
        '''
        print(4, kwargs)
        self.first = value1
        super().__init__(**kwargs)

class ZZ(Z):
    def __init__(self, value2: Any, **kwargs):
        ''' ZZ Class Constructor to initialize the object
        
        Input Values: value2 may be of any type
                      kwargs ...
        '''
        print(3, kwargs)
        self.second = value2
        super().__init__(**kwargs)

class ZZ1(ZZ):
    def __init__(self, value3: Any, value4: Any, **kwargs):
        ''' ZZ1 Class Constructor to initialize the object
        
        Input Values: value3 may be of any type
                      value4 may be of any type
                      kwargs ...
        '''
        print(2, kwargs)
        self.third = value3
        self.fourth = value4
        super().__init__(**kwargs)
    
    
class ZZZ(ZZ1):
    def __init__(self, value5: Any, value6: Any, **kwargs):
        ''' ZZZ Class Constructor to initialize the object
        
        Input Values: value5 may be of any type
                      value6 may be of any type
                      kwargs ...
        '''
        print(1, kwargs)
        self.fifth = value5
        self.sixth = value6
        super().__init__(**kwargs)

class ZZZZ(ZZZ):
    def __init__(self, a: Any, b: Any, c: Any, d: Any, e: Any, f: Any, g: Any):
        ''' ZZZZ Class Constructor to initialize the object
        
        Input Values: a, b, c, d, e, f, g may be of any type
        '''
        kw = {}
        kw["value1"] = a
        kw["value2"] = b
        kw["value3"] = c
        kw["value4"] = d
        kw["value5"] = e
        kw["value6"] = f
        self.seventh = g
        super().__init__(**kw)


demo = ZZZZ(1,2,3,4,5,6,7)
# print(f'demo.first ={demo.first}')
# print(f'demo.second ={demo.second}')
# print(f'demo.third ={demo.third}')
# print(f'demo.fourth ={demo.fourth}')
# print(f'demo.fifth ={demo.sixth}')
# print(f'demo.sixth ={demo.sixth}')
# print(f'demo.seventh ={demo.seventh}')
