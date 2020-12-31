class Fruit:
    """A simple Fruit class"""

    def __init__(self, color: str, smell: str):
        """Fruit Class Constructor to initialize the object.

        Input Arguments: color must be str, smell must be str
        """
        self.color = color
        self.smell = smell
     
    def __repr__(self):
        # return 'Account({!r}, {!r})'.format(self.color, self.smell)
        return self.__class__.__name__

    def print_r(self):
        return 'Account({!r}, {!r})'.format(self.color, self.smell)

    def print_s(self):
        return 'Account({!s}, {!s})'.format(self.color, self.smell)
    
    def print_me(self):
        dummy = ""
        pass
        # return 'Nonsense'
        return '{!a}'.format(self) 

apple = Fruit("Golden Yellow", "Good")
print(apple.print_s)
