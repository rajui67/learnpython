import sys
# some_open = open('some_file.txt', 'x') 
# for write_value in (1,100):
#     some_open.write(write_value)
# close(some_open)    

'''
The 
'''
try: 
    some_open = open('some_file.txt', 'x')
    print(some_open)
except FileExistsError as FE:
#except FileExistsError:
    some_open = open('some_file.txt', 'a')
    print(some_open)
finally: 
    exception_details = sys.exc_info()
    print('finally', exception_details)

for write_value in (1,100):
    some_open.write(str(write_value))
some_open.close() 

