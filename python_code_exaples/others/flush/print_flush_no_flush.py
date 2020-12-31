import time


def count_items_flush(items):

    '''
    This function counts the elements of a tuple passed to it and prints the count.
    It prints a progress indicator equivalent to the length of the tuple before printing the count.
    '''

    print('Counting with flush set to TRUE ', end='', flush=True)
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='', flush=True)

    print(f'\nThere were {num} items')

def count_items(items):

    '''
    This function counts the elements of a tuple passed to it and prints the count.
    The expected output was that all of the print statements would print all at once since the contents of all but the last statement
    are buffered. Instead of the expected output it still prints a progress indicator equivalent to the length of the tuple before 
    printing the count.
    '''

    print('Counting with flush set to false ', end='')
    num = 0
    for item in items:
        num += 1
        time.sleep(1)
        print('.', end='')

    print(f'\nThere were {num} items')

count_items_flush(items=("a", "b", "c", "d", "e"))
count_items(items=("a", "b", "c", "d", "e"))
