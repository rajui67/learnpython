import sys

class DemoWidth:

    def __init__(self, filename: str, mode: str):
        """DemoWidth Class Constructor to initialize the object.

        Input Arguments: filename must be str, filename must be str
        """        
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Inside __enter__')
        self.file_rd = open(self.filename, self.mode)
        return self.file_rd
    
    def __exit__(self, exception_type, exception_value, traceback):
        print('Inside __enter__')
        print(exception_value)
        self.file_rd.close()

with DemoWidth("random.txt", 'w' ) as dw:
    for increment in range(1,11):
        dw.write(f'Counter = {increment}\n')

