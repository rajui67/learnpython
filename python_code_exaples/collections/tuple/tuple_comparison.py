t1 = 10, 215, 20
t2 = 10, 30, "WTF"

print('Will not compare beyond the 2nd element:')
print(f't1 : {t1}, t2 : {t2}, t2 == t1 : {t2 == t1}')
print(f't1 : {t1}, t2 : {t2}, t2 < t1 : {t2 < t1}')
print(f't1 : {t1}, t2 : {t2}, t2 > t1 : {t2 > t1}')
print()

t1 = 19, 215, 20
t2 = 10, 215, "WTF"

print('Will not compare beyond the 1st element:')
print(f't1 : {t1}, t2 : {t2}, t2 == t1 : {t2 == t1}')
print(f't1 : {t1}, t2 : {t2}, t2 < t1 : {t2 < t1}')
print(f't1 : {t1}, t2 : {t2}, t2 > t1 : {t2 > t1}')
print()

t1 = 17, 200, 20
t2 = 17, 200, "WTF"
print('Will work as comparison of values of element# 3 will stop after type comparison and wont go on to compare values')

print(f't1 : {t1}, t2 : {t2}, t2 == t1 : {t2 == t1}', end= '\n\n')
print('Will cause an error, trying to compare 20 with WTF')

t1 = 17, 200, 20
t2 = 17, 200, "20"
print(f't1 : {t1}, t2 : {t2}, t2 < t1 : {t2 < t1}')
print(f't1 : {t1}, t2 : {t2}, t2 > t1 : {t2 > t1}')