import time

def count_items():

    '''
    This function counts the elements of a tuple passed to it and prints the count.
    The expected output was that all of the print statements would print all at once since the contents of all but the last statement
    are buffered. Instead of the expected output it still prints a progress indicator equivalent to the length of the tuple before 
    printing the count.
    '''

    for i in range(1,10):
        time.sleep(1)
        print(i, end=':',flush=False)

print('flush=False')
count_items()
