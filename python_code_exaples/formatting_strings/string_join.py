#import string
s1 = '.'.join(["This", "Is", "Great"])
print(s1)

s2 = '-'.join(x.upper()
              for x in ['This', 'is', 1, None, 0.5, {"key": 1}, 'Great'] if type(x) == str)
print(s2)


