'''
NOTE: Repr() and str() will not work from a script.  print() is the only way to output something to console from a script.
It’s just how Python works. But if you’ll run your script from Python interactive shell and call <object>.repr() or call <object>.str(), 
it will print the results.  It’s just how Python works
'''
from typing import Union

class Account:
    '''A simple account class'''

    def __init__(self, owner:str, amount :Union[int, float]=0):
        """Account Class Constructor to initialize the object.

        Input Arguments: owner must be str, 
                         amount is optional. must be int or float if specified. Default is 0
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        ''' An exaple of overriding the default Object Representation str(<object>), print(<object>)'''
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)

    def __repr__(self):
        ''' An exaple of overriding the default Object Representation repr(<object>)'''
        return 'Account({}, {})'.format(self.owner, self.amount)



acc = Account('bob', 10)
str(acc)
print(acc)
repr(acc)

another_acc = Account('Ganesh', 20)
print(another_acc)
repr(another_acc)

    