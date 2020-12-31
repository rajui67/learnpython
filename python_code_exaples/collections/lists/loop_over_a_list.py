#!/usr/bin/env python
print("Hello World")
words = ['a', 'b', 'c', 'd']

print("\nSimple iteration over elements of a list")
for w in words:
   print(w)

print("\nOne way of looping over a list and displaying the element value and postion of the element")

i = 0
for w in words:
    print(w,i)
    i = i + 1

print("\nAnother way of looping over a list and displaying the element value and postion of the element using the range function")
print(len(words))
for i in range(len(words)):
    print(words[i],i)


print("\nRECOMMENDED WAY OF LOOPING OVER A LIST WHEN A COUNTER IS NEEDED IS TO USE THE ENNUMERATE FUNCTION: SEE FILE ennumerate_list.py")


