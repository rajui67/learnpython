
'''
UPDATE:
There is a bug with the warlus operator: https://bugs.python.org/issue?%40columns=id%2Cactivity%2Ctitle%2Ccreator%2Cassignee%2Cstatus%2Ctype&%40sort=-activity&%40filter=status&%40action=searchid&ignore=file%3Acontent&%40search_text=walrus&submit=search&status=-1%2C1%2C2%2C3
There are other cases of erroneous behavior when the walrus operator is used without enclosing them in parentheses.
CONCLUSION: Always enclose assignment expressions within parantheses. e.g.; if (boolean := true) and not if boolean := true
END UPDATE

Details of Python beahvior when an assignment expression (warlus operator :=) is used within a conditional 

The print statement in the following code snippet generates an error:

###
array2 = [8, 9, 10, 11, 12, 13, 14]
#print(f'{array3[:3] if array3 := [*array2].reverse() else None}')

# ends with the error
# Actual Results:
# ended with an error; the output produced was as follows:
# File “”, line 1
# (array3[:3] if array3 )
# ^
# SyntaxError: unexpected EOF while parsing
###

The reason (just a guess validated with test ) for the syntax error is because of the way python reads the conditional expression. It reads:

    if array3 := [*array2].reverse() else None
    thus so:
    if array:
        #everything after the : comes down here
        = [*array2].reverse()
    else:
    None

What you expected was for it to be interpreted thus so:

    if (array3 := thing):
    else: None

To test the hypotheses that this is how the interpreter interprets an assignment expression embedded in a conditional expression, 
I added an in-line assignment to the else part of the conditional expression and another in-line assignment outside of the conditional expression. 
Without the parentheses, the else part fails; the “:” part of the walrus operator causes Python behavior in line with your explanation. 
Outside of the conditional expression, the assignment expression works without having to enclose the operation in parentheses.
'''

array2 = [8, 9, 10, 11, 12, 13, 14]
#print(f'{array3[:3] if array3 := [*array2].reverse() else None}') # fails
# print(dummy := 3, f'{array3[:3] if (array3 := [*array2].reverse()) else array4 := [1,2]}') # this too fails

# dummy := 3 is inside 
print(dummy := 3, f'{array3[:3] if (array3 := [*array2].reverse()) else (array4 := [1,2])}') # succeeds