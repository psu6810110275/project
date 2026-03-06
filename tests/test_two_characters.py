import unittest
from coe_6810110275.two_characters import alternate

class TwoCharactersTest(unittest.TestCase):
    
    def test_give_beabeefeab_should_be_5(self):
        # Arrange 
        s = 'beabeefeab'
        expected_output = 5
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_a_should_be_0(self):
        # Arrange 
        s = 'a'
        expected_output = 0
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_ab_should_be_2(self):
        # Arrange 
        s = 'ab'
        expected_output = 2
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_aa_should_be_0(self):
        # Arrange 
        s = 'aa'
        expected_output = 0
        
        # Act
        result = alternate(s)
        
        # Assert
        self.assertEqual(result, expected_output)
