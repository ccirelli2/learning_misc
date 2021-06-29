"""
Examples using built in unittest library
"""

###############################################################################
# Import Libraries
###############################################################################
import logging
logging.basicConfig(level=logging.INFO)
import unittest


###############################################################################
# Unit tests
###############################################################################
"""
Requirements of this tester:  Arguments must be a class object that inherits
    from unittest.TestCase.  Also, the first method must take as an input
    self and use one of the unittest library asset statements in place of the
    built in assert class.
"""

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)), 6, "Should be 6")





if __name__ == "__main__":
    unittest.main()
