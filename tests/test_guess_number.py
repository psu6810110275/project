import unittest
from unittest.mock import patch
from coe_6810110275.guess_number import guess_int, guess_float

class RandomUtilsTest(unittest.TestCase):
    
    @patch('coe_6810110275.random_utils.random.randint')
    def test_guess_int_should_return_mocked_value(self, mock_randint):
        mock_randint.return_value = 5
        start, stop = 1, 10
        expected_output = 5
        
        # Act
        result = guess_int(start, stop)
        
        # Assert
        self.assertEqual(result, expected_output)
        mock_randint.assert_called_once_with(start, stop)

    @patch('coe_6810110275.random_utils.random.uniform')
    def test_guess_float_should_return_mocked_value(self, mock_uniform):
        # Arrange
        mock_uniform.return_value = 3.14
        start, stop = 1.0, 5.0
        expected_output = 3.14
        
        # Act
        result = guess_float(start, stop)
        
        # Assert
        self.assertEqual(result, expected_output)
        mock_uniform.assert_called_once_with(start, stop)
