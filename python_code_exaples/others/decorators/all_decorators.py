'''
Module to house all decorator functions used by other modules in this package
'''

def this_decorates_that(func):
    ''' Decorates a function
    Inputs: func is function
    '''
    def this_is_the_decoaration():
        print("1")
        func()
        print("2")
    return this_is_the_decoaration

def decoratator_with_ability_to_pass_parameters(func, *args, **kwargs):
    ''' Decorates a function. 
    Inputs: func is function
    '''
    def decorate(*args, **kwargs):
        print("1")
        func(*args, **kwargs)
        print("2")
    return decorate

def decoratator_with_ability_to_pass_parameters_and_return_values(func, *args, **kwargs):
    ''' Decorates a function. 
    Inputs: func is function
    '''
    def decorate(*args, **kwargs):
        print("1")
        ret_val = func(*args, **kwargs)
        print("2")
        return ret_val
    return decorate