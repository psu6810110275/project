import unittest
from coe_6810110275.fizzbuzz import fizzbuzz

class FizzBuzzTest(unittest.TestCase):
    
    def test_give_3_should_return_fizz(self):
        # Arrange
        x = 3
        expected_output = "Fizz"
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should return {expected_output}')

    def test_give_5_should_return_buzz(self):
        # Arrange
        x = 5
        expected_output = "Buzz"
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should return {expected_output}')

    def test_give_15_should_return_fizzbuzz(self):
        # Arrange
        x = 15
        expected_output = "FizzBuzz"
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should return {expected_output}')

    def test_give_2_should_return_2_string(self):
        # Arrange
        x = 2
        expected_output = "2"
        
        # Act
        result = fizzbuzz(x)
        
        # Assert
        self.assertEqual(result, expected_output, f'Should return {expected_output}')

# if __name__ == '__main__':
#     unittest.main()
