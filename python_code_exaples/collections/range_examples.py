#!/usr/bin/env python
print("Experiment with range function", "\n")
print("one value given to range function")
for i in range(5):
    print(i)

for i in range(stop = 5):
    print(i)

print("\nexplicitly specify a different start value\n")
for i in range(1,5):
    print(i)

print("\nexplicitly specify a different start value AND a different increment by value\n")
for i in range(1,5,2):
    print(i)

