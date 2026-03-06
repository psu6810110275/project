import unittest
from coe_6810110275.caesar_cipher import caesarCipher

class CaesarCipherTest(unittest.TestCase):
    
    def test_give_middle_outz_k_2_should_be_okffng_qwvb(self):
        # Arrange
        s = 'Middle-Outz'
        k = 2
        expected_output = 'Okffng-Qwvb'
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_always_look_on_the_bright_side_of_life_k_5(self):
        # Arrange
        s = 'Always-Look-On-The-Bright-Side-Of-Life'
        k = 5
        expected_output = 'Fqbfdx-Qttp-Ts-Ymj-Gwnlmy-Xnij-Tk-Qnkj'
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_hello_world_k_87_should_wrap_around(self):
        # Arrange
        s = 'Hello_World!'
        k = 87 
        expected_output = 'Qnuux_Fxaum!'
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)

    def test_give_symbols_only_k_10_should_remain_unchanged(self):
        # Arrange
        s = '1234!@#$-'
        k = 10
        expected_output = '1234!@#$-'
        
        # Act
        result = caesarCipher(s, k)
        
        # Assert
        self.assertEqual(result, expected_output)
