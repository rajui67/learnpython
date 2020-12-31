'''
Of the  ways of handling exceptions that may arise within a with code block. is one way preferable t0 another?

Martin Breuss at codingnomads prefered #1:
because it wraps the try-except block around where the error actually takes place. 
As you wrote in your comment, the exception “is not related to file operations”, so it makes sense to keep the try-except block focused on what it’s catching.
e.g. You could add another try-except for catching a potential IOError, if that’s something you wanted to handle as well.
'''



###
##  "try except" enclosed within "with" code block
###
full_path_file_name = "/home/riyer/python_code_exaples/file_operations/random.txt"
with  open(full_path_file_name,"r+") as file_rd2:
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
full_path_file_name = "/home/riyer/python_code_exaples/file_operations/random.txt"
try:
    with  open(full_path_file_name,"r+") as file_rd3:
        content = file_rd3.read()    
        print('2', 'opened file: with statement', content)
        raise IndexError # Simulating an exception that is not related to file operations 
except IndexError as Ie :
    pass    # stand in for exception handling

print(type(file_rd3), id(file_rd3))
The variables (file_rd2, file_rd3) 

