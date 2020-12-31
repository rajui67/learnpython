
start, end = 10000, 10006

print('\nPrint integers with float format option "e" (space before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i:,e};', end='')

print('\nPrint integers with float format option "E" (space before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i:,E};', end='')

print('\nPrint integers with float format option "f" (space before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i:,f};', end='')

print()
