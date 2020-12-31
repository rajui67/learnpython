
start, end = 10000, 10006

print('\nPrint integers with sign format = " " (space before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i: ,d};',end='')

print('\nPrint integers with sign format = "+" (+ before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i:+,d};',end='')

print('\nPrint integers with sign format = "-" (""<none> before +ve - before -ve):')
for i in range(start, end):
    print(f'{i if i % 2 else -1 * i:-,d};',end='')

print()
