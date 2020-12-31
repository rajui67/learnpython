import sys
from typing import Optional
class DemoWidth:

    def __init__(self, filename: str, mode: str, write_this_also: Optional[str] = "Chumma"):
        """DemoWidth Class Constructor to initialize the object.

        Input Arguments: filename must be str, mode must be  str, 
                         write_this_also is optional. Must be str if specified. Default value is "Chumma"
        """        
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file_rd = open(self.filename, self.mode)
        return self.file_rd 
    
    def __exit__(self, exception_type, exception_value, traceback): ## Why TypeError: __exit__() takes 1 positional argument but 4 were given
        self.file_rd.close()

    def write (string: str):
        self.file_rd(string, write_this_also)    

with DemoWidth("random.txt", 'w' ) as dw:
    # print(dw)  # <_io.TextIOWrapper name='random.txt' mode='w' encoding='UTF-8'> dict_items([('mode', 'w')])
    for increment in range(1,10):
        dw.write(f'Counter = {increment}')


dw1 = DemoWidth("random1.txt", "w")
print(dw1.filename)