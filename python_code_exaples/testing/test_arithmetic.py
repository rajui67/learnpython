import unittest

def subtract_divide(dividend, first, second):
    try:
        quotient = first - second
        return dividend / quotient
    # except ZeroDivisionError:
    #     raise ZeroDivisionError
    except ZeroDivisionError:
        return f"this won't work, {first} - {second} is 0 or lower."

class TestArithmetic(unittest.TestCase):
    # Returns OK If the call to test_subtract_divide results in 5 
    def test_subtract_divide(self):
        self.assertEqual(subtract_divide(dividend=10, first=4, second=2), 5)
   
if __name__ == '__main__':
    unittest.main()


        