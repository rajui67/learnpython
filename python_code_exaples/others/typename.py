
'''
Function to return the typename of an object/instance  
'''
# from typing import Any
# def typename(derive_the_typename_of_this_instance: Any,/) -> str: 

import typing
def typename(derive_the_typename_of_this_instance: typing.Any,/) -> str: 
    ''' 
    Given a varaible of any type, returns the type name of the variable.

    e.g.:

    Note the function parmater is position only typename(derive_the_typename_of_this_instance  = "")
TypeError: typename() got some positional-only arguments passed as keyword arguments: 'derive_the_typename_of_this_instance'
    '''
    typeof =str(type(derive_the_typename_of_this_instance))
    split_it_up = typeof.split("'")
    intermediate_name_derived = split_it_up[1]
    final_name_derived = intermediate_name_derived.split(".")[-1]
    return final_name_derived

# The same functionally implemented in an extremely cryptic form can be:  
# def typename(derive_the_typename_of_this_instance): return str(type(derive_the_typename_of_this_instance)).split("'")[1].split(".")[-1]

