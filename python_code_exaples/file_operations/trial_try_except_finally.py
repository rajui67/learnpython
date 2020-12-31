file_path_to_file = "/home/riyer/python_code_exaples/file_operations/random.txt"
try:
    file_rd = open(file_path_to_file,"r+")
    content = file_rd.read()    
    print('1', content)
    raise IndexError # Simulating an exception that is not related to file operations 
    # file_rd.close() # execution will never reach here because exception has been raised

except IndexError as Ie :
    pass    # stand in for exception handling
finally:
   file_rd.close()
