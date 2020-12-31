'''
WARNING: The second invocation of locals() 'copy_of_locals = locals()' resets copy_wtf to an exact copy of copy_of_locals. Explaination

 https://docs.python.org/3/library/functions.html#locals 

Note that modifying the locals dictionary is undefined behavior in python, so this line of code: copy_wtf["demo_var"] = "bar" is “undefined”. 
What that means is… well it could be anything. It could work fine, it could crash the program, it could lead to some corruption of internal structures.
But anyhow, you are getting a pointer to a dictionary that is maintained by the compiler. Since the compiler is counting on you NOT modifying this structure, 
it makes no sense for it to give you back a new dictionary each time (it’s a waste of memory). 
So it is likely just modifying the dictionary in place and giving you back the same reference. 
This is likely an optimization. This only works because you are not supposed to modify the dictionary. 
BTW, I am guessing this because the verbiage hints at it in the docs: 
“Update and return a dictionary representing the current local symbol table.” Seems like they are updating an internal structure, and giving you back a reference. 
You’d have to check the Python source code to know for sure.

If you did want to make an actual copy, you could use copy:

    from copy import copy

    def demo_locals():
        demo_var = 'foo'
        copy_wtf = copy(locals())
        copy_wtf['demo_var'] = 'bar'
        print("1: ", f"copy_wtf = {copy_wtf}")
        copy_of_locals = copy(locals())
        print(f"2: copy_wtf = {copy_wtf}", f"copy_of_locals = {copy_of_locals}", sep = ' || ')
        print(copy_wtf == copy_of_locals)
        print(demo_var)

    demo_locals()
'''


def demo_locals():
    '''This function demonstrates that the built-in function locals() returns a COPY of the local namespace and not a pointer to the local namespace. 
    (The local namespace is maintained as a dict)'''
    demo_var = 'foo'
    copy_wtf = locals()
    copy_wtf['demo_var'] = 'bar'
    print('1: ', f'''copy_wtf =  {copy_wtf}''')
    copy_of_locals = locals()
    print(f'''2:  copy_wtf =  {copy_wtf}''', f'''copy_of_locals = {copy_of_locals}''', sep = ' || ')

demo_locals()
