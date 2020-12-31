from typing import Any
def typename(derive_the_typename_of_this_instance: Any,/) -> str: 
    ''' 
    Function to return the typename of an object/instance  
    Given a varaible of any type, returns the type name of the variable.

    e.g.:
        test_this = []
        typeof = typename(test_this)
        will return the string 'list'

    Note: the function parmater is positional only:
        typename(derive_the_typename_of_this_instance  = <something>)
        Will generate the error TypeError: typename() got some positional-only arguments passed as keyword arguments: 'derive_the_typename_of_this_instance'
    '''
    typeof =str(type(derive_the_typename_of_this_instance))
    split_it_up = typeof.split("'")
    intermediate_name_derived = split_it_up[1]
    final_name_derived = intermediate_name_derived.split(".")[-1]
    return final_name_derived

# The same functionally implemented in an extremely cryptic form can be:  
# def typename(derive_the_typename_of_this_instance): return str(type(derive_the_typename_of_this_instance)).split("'")[1].split(".")[-1]

