import unittest
from coe_6810110275.cat_and_mouse import cat_and_mouse

class CatAndMouseTest(unittest.TestCase):
    
    def test_cat_b_catches_mouse(self):
        # Arrange
        x, y, z = 1, 2, 3
        expected_output = "Cat B"
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_mouse_escapes(self):
        # Arrange
        x, y, z = 1, 3, 2
        expected_output = "Mouse C"
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_cat_b_catches_mouse_again(self):
        # Arrange
        x, y, z = 1, 5, 4
        expected_output = "Cat B"
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, expected_output)
        
    def test_cat_a_catches_mouse(self):
        # Arrange
        x, y, z = 2, 5, 3
        expected_output = "Cat A"
        
        # Act
        result = cat_and_mouse(x, y, z)
        
        # Assert
        self.assertEqual(result, expected_output)
