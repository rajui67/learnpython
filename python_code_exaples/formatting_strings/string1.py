income = 12 * 8900
tax = int(income * .3) 

print("\nSTRING FORMATTING, OLD STYLE (DEPRECATED):\n")
text_os1 = 'Your yearly income is %s and tax is %s' % (income, tax)
print('Old style string formatting using %s', text_os1, sep=': ')

text_os2 = 'Your yearly income is %(print_income)s and tax is %(print_tax)s' % { 
    "print_income": income, "print_tax": tax } # "income": income, "tax": tax will also work
print('Old style string formatting using %(<varible_name>)s', text_os2, sep=': ')

print("\nSTRING FORMATTING, NEW STYLE (str.format):\n")
text_f1 = 'Your yearly income is {} and tax is {}'.format(income, tax)
print('New style string formatting using empty braces', text_f1, sep=': ')

text_f2 = 'Your yearly income is {fs2_income} and tax is {fs2_tax}'.format(fs2_income = income, fs2_tax = tax)
print('New style string formatting using names in braces', text_f1, sep=': ')

print("\nSTRING FORMATTING, NEW STYLE (f-string):\n")
text_fs1 = f'Your yearly income is {income} and tax is {tax}'
print('New style string formatting using f-string', text_fs1, sep=': ')