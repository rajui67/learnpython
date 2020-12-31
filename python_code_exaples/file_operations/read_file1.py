'''
Example of a simple with statement. The advantage of using a with statement to open files  is that the file is autiomatically closed after statements in the with code block is executed. 
It is another way of performing "try finally"  
'''

###
# "try except" enclosed within "with" code block
###
file_path_to_file = "/home/riyer/python_code_exaples/file_operations/random.txt"
with  open(file_path_to_file,"r+") as file_rd2:
    try:
        content = file_rd2.read()    
        print('1', 'opened file: with statement', content)
        raise IndexError # Simulating an exception that is not related to file operations 
    except IndexError as Ie :
        pass    # stand in for exception handling

print(type(file_rd2), id(file_rd2))

###
# "with" enclosed within "try" code block 
###
file_path_to_file = "/home/riyer/python_code_exaples/file_operations/random.txt"
try:
    with  open(file_path_to_file,"r+") as file_rd3:
        content = file_rd3.read()    
        print('2', 'opened file: with statement', content)
        raise IndexError # Simulating an exception that is not related to file operations 
except IndexError as Ie :
    pass    # stand in for exception handling

print(type(file_rd3), id(file_rd3))


###
# open fil without using the with statement
###
file_path_to_file = "/home/riyer/python_code_exaples/file_operations/random.txt"
file_rd3 = None
try:
    file_rd3 = open(file_path_to_file,"r+")
    content = file_rd3.read()    
    print('3', 'opened file: try statement', content)
    raise IndexError # Simulating an exception that is not related to file operations 
    file_rd3.close() # execution will never reach here because exception has been raised
except IndexError as Ie :
    pass    # stand in for exception handling
finally:
    if file_rd3 and  file_rd3.closed == False:
        file_rd3.close()

print(type(file_rd3), id(file_rd3))

