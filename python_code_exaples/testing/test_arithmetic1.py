'''
Test of Pylint using a custom module
'''

import unittest

from others import arithmetic


class TestArithmetic(unittest.TestCase):
    '''Unit test cases for arithmetic module
    '''

    # Returns OK If the call to test_subtract_divide results in 5
    def test_subtract_divide(self):
        '''verify that method subtract_divide works as expected '''
        self.assertEqual(arithmetic.subtract_divide(dividend=10, first_number=4, second_number=2), 5)

    # Returns OK if the call raises the error else returns FAILED.
    def test_subtract_divide_zerodiv(self):
        '''verify that method raises ZeroDivisionError'''
        self.assertRaises(ZeroDivisionError, arithmetic.subtract_divide, 10, 4, 4)

    # NOTE:The second argument passed to TestArithmetic is the result of calling the function result

    # def setUp(self):
    #     '''setup steps to run for every test case'''
    #     print('Pretending to do some setup. I run for every test case')

    # def tearDown(self):
    #     '''Housekeeping tasks after every test case'''
    #     print('Pretending to do some housekeeping. I run for every test case')

    # @classmethod
    # def setUpClass(cls):
    #     '''setup steps to run once at the begining of these tests'''
    #     print('Run once before any of the tests in this file execute:', cls)

    # @classmethod
    # def tearDownClass(cls):
    #     '''setup steps to run once at the end of these tests'''
    #     print('Run once before after all of the tests in this file execute:', cls)

if __name__ == '__main__':
    unittest.main()
