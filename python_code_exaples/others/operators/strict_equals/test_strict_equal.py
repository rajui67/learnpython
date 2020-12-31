from strict_equal import strict_equal

integer = 1234
string_integer = '1234'
boolean = True
floating = 1234.0
tuple1 = 17, 200, 20
none = None

print(f'floating: {floating}, integer: {integer}, floating == integer: {floating == integer}')
print(f'integer: {integer}, floating: {floating}, integer == floating: {integer == floating}')
print(f'strict_equal(a, b): {strict_equal(integer, integer)}')
print(f'strict_equal(a, b): {strict_equal(integer, floating)}')