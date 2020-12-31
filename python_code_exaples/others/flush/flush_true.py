import time

def count_items_flush():

    '''
    This function counts the elements of a tuple passed to it and prints the count.
    It prints a progress indicator equivalent to the length of the tuple before printing the count.
    '''
    for i in range(1,10):
        time.sleep(1)
        print(i, end=':', flush=True)

print('flush=True')
count_items_flush()


