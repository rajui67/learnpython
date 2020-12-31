
import os
os.system('clear')

def multiplier_sequence(multiplicand: int):
    '''
        Demonstrate yield and send
    '''
    multiplier = 1
    while True:
        product = multiplier * multiplicand
        value_received = (yield product)
        if value_received is not None:
            multiplier = value_received
        multiplier += 1


gen_div = multiplier_sequence(3)


# Without the next send will generate this error
# File "/home/riyer/learnpython/python_code_exaples/generators/send_using_for_loop_on_range.py", line 19, in <module>
#       print('The value returned by the send method =', it_val := gen_div.send(4))
#    TypeError: can't send non-None value to a just-started generator
it_val = next(gen_div)
print(it_val)
for counter in range(3):
    print('The value returned by the send method =', it_val := gen_div.send(counter + 4))



