def printit(string):
    '''
    This  is an exaple of defining a function without using python type hinting. 
    '''
    my_string = 'Ha'
    string += ' ' + my_string
    print(string)

my_string = 'Nonsense'
printit(my_string)
print(my_string)
