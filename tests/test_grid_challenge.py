import unittest
from coe_6810110275.grid_challenge import gridChallenge

class GridChallengeTest(unittest.TestCase):
    
    def test_give_valid_grid_should_be_yes(self):
        # Arrange 
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = 'YES'
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_invalid_grid_should_be_no(self):
        # Arrange 
        grid = ['mpxz', 'abcd', 'wlmf']
        expected_output = 'NO'
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_single_row_should_be_yes(self):
        # Arrange 
        grid = ['zyx']
        expected_output = 'YES'
        
        # Act
        result = gridChallenge(grid)
        
        # Assert
        self.assertEqual(result, expected_output)
