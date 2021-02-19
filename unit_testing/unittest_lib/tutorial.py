"""
Description : Tutorial on unit testing.
Ref : https://realpython.com/python-testing/
Built in library : https://docs.python.org/3/library/unittest.html
Python Assertion: https://www.w3schools.com/python/ref_keyword_assert.asp
    https://www.tutorialspoint.com/python/assertions_in_python.htm

Notes:

    Unit Test: small test that checks that a single component operates
        in the right way.  A unit test helps you to isolate what is broken
        in your application and fix it faster.


    Assetion Statement: raise-if_not statement.  An expression is tested and if
        the result comes up false, an exception is raised.  It is used for
        testing code.  Programmers often place assertions at teh start of a
        function to check for valid input and after a function to call to check
        for valid output.

        Note: Assetion statements can be handled like any other exception
            using a try-except statement.  ***That said, if not handled,
            they will terminate the program and produce a traceback error.

    Test Runner: special application designed for running tests, checking
        output and giving tools for debugging and diagnosing tests and
        applications.

        unittest:
            Build in python library.  Requires that you put your tests into
            classes as methods.
            You use a series of special assertion methods in the
            unittest.TestCase class instead of the built-in asset statement.


"""
###############################################################################
# Import Python Libraries
###############################################################################
import logging
logging.basicConfig(level=logging.DEBUG)
import unittest

###############################################################################
# Functions
###############################################################################

# Example of Assettion Statement Used For Unit Testing
def unit_test_sum_operation(list_ints):

    # Test Input of Function
    try:
        assert isinstance(list_ints, list)
        logging.debug(f'correct datatype list passed to function unit_test')
    except AssertionError as err:
        logging.error('Assertion error on input to function unit test.')

    # Perform a separate unit test:
    try:
        assert sum([1,2,3]) == 6, "should be 6"
        logging.debug(f'unit test passed for sum function within unit_test')
    except AssertionError as err:
        logging.error('Assertion error on sum() of known input')


unit_test_sum_operation([1,2,3])






























