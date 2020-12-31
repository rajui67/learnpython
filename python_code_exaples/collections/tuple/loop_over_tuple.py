import os
os.system('clear')
family ='mother', 'father', 'son', 'daughter'

print('Iterating over a tuple:')
for member in family:
    print(member)

print('\nIterating over enumarated class of a tuple:')
for member in enumerate(family):
    print(member[1])

print('\nIterating over enumarated class converted to a list:')
for member in list(enumerate(family)):
    print(member[1])

print('Here')


''' values generated:

Iterating over a tuple:
mother
father
son
daughter

Iterating over enumarated class of a tuple:
mother
father
son
daughter

Iterating over enumarated class converted to a list:
mother
father
son
daughter
Here
'''