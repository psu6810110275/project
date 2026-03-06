import unittest
from coe_6810110275.alternating_characters import alternatingCharacters

class AlternatingCharactersTest(unittest.TestCase):
    
    def test_give_AAAA_should_be_3_deletions(self):
        # Arrange
        s = 'AAAA'
        expected_output = 3
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_BBBBB_should_be_4_deletions(self):
        # Arrange
        s = 'BBBBB'
        expected_output = 4
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_ABABABAB_should_be_0_deletions(self):
        # Arrange
        s = 'ABABABAB'
        expected_output = 0
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_AAABBB_should_be_4_deletions(self):
        # Arrange
        s = 'AAABBB'
        expected_output = 4
        
        # Act
        result = alternatingCharacters(s)
        
        # Assert
        self.assertEqual(result, expected_output)
