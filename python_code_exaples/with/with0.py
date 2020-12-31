import sys

with open('file_path', 'w') as file: 
    file.write('hello world !') 
    
try:
    file.write('hello universe !') 
except ValueError as ve:
    err = sys.exc_info()
    print(sys.exc_info()[1])