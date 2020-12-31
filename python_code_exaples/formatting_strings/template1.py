from string import Template
income = 1000
tax = 300
print("\nSTRING FORMATTING, NEW STYLE (TEMPLATE):\n")
print("Method 1:")
text_t1 = 'Your yearly income is $t1_income and tax is $t1_tax'
print(text_t1, Template(text_t1).substitute(t1_income=income, t1_tax=tax), sep=": ")

print("\nMethod 2:")
text_t2 = Template('Your yearly income is $t1_income and tax is $t1_tax')
print(text_t2.template, text_t2.substitute(t1_income=income, t1_tax=tax), sep=": ")