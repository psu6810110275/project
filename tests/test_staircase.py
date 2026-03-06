import unittest
from coe_6810110275 import staircase

class StaircaseTest(unittest.TestCase):
    
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = '#'
        expected_output = \
         " #\n" + \
         "##"
        
        # act
        result = staircase.staircase(n, pattern)
        
        # assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_3_with_star_should_be_stars(self):
        # arrange
        n = 3
        pattern = '*'
        expected_output = \
         "  *\n" + \
         " **\n" + \
         "***"
         
        # act
        result = staircase.staircase(n, pattern)
        
        # assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
