from assert_example import strict_equal
import sys
integer = 1234
string_integer = '1234'
boolean = True
floating = 1234.0
tuple1 = 17, 200, 20
none = None

print(f'floating: {floating}, integer: {integer}, floating == integer: {floating == integer}')
print(f'integer: {integer}, floating: {floating}, integer == floating: {integer == floating}')
try:
    print(f'strict_equal(a, b): {strict_equal(integer, integer)}')
except:
    ex_name, ex_message, ex_stack = sys.exc_info()
    print('ex_message =', ex_message)

print(f'strict_equal(a, b): {strict_equal(integer, floating)}')