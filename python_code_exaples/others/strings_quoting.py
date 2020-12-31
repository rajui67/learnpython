import os
os.system("clear")
print('''This is a trial of
         the triple quote feature''')
print()
print(('This is a trial of enclosing '
       'strings in () feature '))
print()

## in variables
triple_quoted_string = '''
This is an example of populating
a variable with values using triple quotes'''

print(triple_quoted_string)

if True:
    triple_quoted_string = '''
    This is an example of populating
    a variable with values using triple quotes when indented
    Note that the spaces before the indentation are also printed'''

    print()
    print(triple_quoted_string)

if True:
    triple_quoted_string = ('This is a neater example of populating\n'
                            'a variable with values by enclosing the strings '
                            'in parantheses (): \n'
                            'It prints without the indentaion but note that linefeed character \\n '
                            'needs to be used, else thes string is printed all in one line, like so: \n')
    print()
    print(triple_quoted_string)

    triple_quoted_string = ('This is a neater example of populating'
                            'a variable with values by enclosing the strings '
                            'in parantheses (): '
                            'It prints without the indentaion but note that linefeed character \\n '
                            'needs to be used, else thes string is printed all in one line, like so: ')
    print()
    print(triple_quoted_string)