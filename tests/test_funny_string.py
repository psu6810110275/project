import unittest
from coe_6810110275.funny_string import funnyString

class FunnyStringTest(unittest.TestCase):
    
    def test_give_acxz_should_be_funny(self):
        # Arrange
        s = 'acxz'
        expected_output = 'Funny'
        
        # Act
        result = funnyString(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_bcxz_should_be_not_funny(self):
        # Arrange
        s = 'bcxz'
        expected_output = 'Not Funny'
        
        # Act
        result = funnyString(s)
        
        # Assert
        self.assertEqual(result, expected_output)
