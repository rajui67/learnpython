
import os
os.system('clear')

def multiplier_sequence(multiplicand: int):
    '''
        This function is a pretend function to demonstrate 
    '''
    multiplier = 1
    while True:
        product = multiplier * multiplicand
        value_received = (yield product)
        if value_received is not None:
            multiplier = value_received
        multiplier += 1

gen_div = multiplier_sequence(3)
while True:
    print('The value returned by the send method =', it_val := gen_div.send(None))
    if it_val == 9:
        break
        


