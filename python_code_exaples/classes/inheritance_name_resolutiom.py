
# Python program showing 
# how MRO works 
  
class Parent: 
    pass
    def rk(self): 
        print(f"1: In class Parent. self is from {self.__class__.__name__}") 

class Child(Parent): 
    pass
    def rk(self): 
        print(f"2: In class Child. self is from {self.__class__.__name__}") 

class GrandChild(Child): 
    pass
    def rk(self): 
        print(f"3: In class GrandChild. self is from {self.__class__.__name__}") 

class GreatGrandChild(GrandChild): 
    pass
    # def rk(self): 
    #     print(f"4: In class GreatGrandChild. self is from {self.__class__.__name__}") 

class GtGtGrandChild(GreatGrandChild): 
    pass
     
rslv = GtGtGrandChild() 
rslv.rk() 
print(isinstance(rslv, GtGtGrandChild))
print(isinstance(rslv, GreatGrandChild))
print(isinstance(rslv, GrandChild))
print(isinstance(rslv, Child))
print(isinstance(rslv, Parent))

print(issubclass(GtGtGrandChild, GtGtGrandChild))
print(issubclass(GtGtGrandChild, GreatGrandChild))
print(issubclass(GtGtGrandChild, GrandChild))
print(issubclass(GtGtGrandChild, Child))
print(issubclass(GtGtGrandChild, Parent))