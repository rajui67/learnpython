integer = 1234
string_integer = '1234'
boolean = True
floating = 1234.0
tuple1 = 17, 200, 20
none = None

# integer to string value comparison is never true despite having values that are the same.
print(f'integer: {integer}, string_integer: "{string_integer}", integer == string_integer: {integer == string_integer}', end = "\n\n")
print(f'string_integer: "{string_integer}", integer: {integer}, string_integer == integer: {string_integer == integer}', end = "\n\n")

print(f'integer: {integer}, string_integer: "{string_integer}", integer != string_integer: {integer != string_integer}', end = "\n\n")
print(f'string_integer: "{string_integer}", integer: {integer}, string_integer != integer: {string_integer != integer}', end = "\n\n")

# TypeError: '<' not supported between instances of 'int' and 'str'
# print(f'integer: {integer}, string_integer: "{string_integer}", integer < string_integer: {integer < string_integer}', end = "\n\n")
# print(f'string_integer: "{string_integer}", integer: {integer}, string_integer < integer: {string_integer < integer}', end = "\n\n")

# TypeError: '>' not supported between instances of 'int' and 'str'
# print(f'integer: {integer}, string_integer: "{string_integer}", integer > string_integer: {integer > string_integer}', end = "\n\n")
# print(f'string_integer: "{string_integer}", integer: {integer}, string_integer > integer: {string_integer > integer}', end = "\n\n")


print(f'integer: {integer}, boolean: {boolean}, integer == boolean: {integer == boolean}', end = "\n\n")
print(f'boolean: {boolean}, integer: {integer}, boolean == integer: {boolean == integer}', end = "\n\n")

print(f'integer: {integer}, none: {none}, integer == none: {integer == none}', end = "\n\n")
print(f'none: {none}, integer: {integer}, none == integer: {none == integer}', end = "\n\n")

print(f'floating: {floating}, integer: {integer}, floating == integer: {floating == integer}', end = "\n\n")
print(f'integer: {integer}, floating: {floating}, integer == floating: {integer == floating}', end = "\n\n")



# def strict_equal(a, b):
#     assert (type(a) == type(b))
#     return (a == b)

# print(f'strict_equal(a, b): {strict_equal(integer, integer)}', end = "\n\n")