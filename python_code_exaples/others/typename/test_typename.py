# derive_the_typename_of_this_variable = '''<class '_io.TextIOWrapper'>'''
from typename import typename

class Test:
    def __init__(self):
        """Test Class Constructor to initialize the object.

        Input Arguments: None
        """        
        pass

    def __str__(self):
        pass

class ChildOfTest(Test):
    def __init__(self):
        """ChildOfTest Class Constructor to initialize the object.

        Input Arguments: None
        """        
        pass

    def __str__(self):
        pass

derive_the_typename_of_this_variable = 1
typeof = typename(derive_the_typename_of_this_variable)
print(200, typeof)

derive_the_typename_of_this_variable = []
typeof = typename(derive_the_typename_of_this_variable)
print(300, typeof)

derive_the_typename_of_this_variable = (None,)
typeof= typename(derive_the_typename_of_this_variable)
print(400, typeof)

derive_the_typename_of_this_variable = {}
typeof = typename(derive_the_typename_of_this_variable)
print(500, typeof)

derive_the_typename_of_this_variable = Test()
typeof = typename(derive_the_typename_of_this_variable)
print(600, typeof)

derive_the_typename_of_this_variable =  ChildOfTest()
typeof = typename(derive_the_typename_of_this_variable)
print(700, typeof)

derive_the_typename_of_this_variable = iter((None,))
typeof = typename(derive_the_typename_of_this_variable)
print(800, typeof)

derive_the_typename_of_this_variable = iter({"dummy": "dummy"})
typeof = typename(derive_the_typename_of_this_variable)
print(900, typeof)

derive_the_typename_of_this_variable = iter([])
typeof = typename(derive_the_typename_of_this_variable)
print(1000, typeof)

derive_the_typename_of_this_variable = iter({10,20})
typeof = typename(derive_the_typename_of_this_variable)
print(1100, typeof)

derive_the_typename_of_this_variable = iter("")
typeof = typename(derive_the_typename_of_this_variable)
print(1200, typeof)
