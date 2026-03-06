from coe_6810110275.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_2_3_5_is_prime(self):
        prime_list = [2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_prime(self):
        not_prime_list = [4, 6, 8]
        is_prime = is_prime_list(not_prime_list)
        self.assertFalse(is_prime)

    def test_give_2_3_4_is_not_prime(self):
        mixed_list = [2, 3, 4]
        is_prime = is_prime_list(mixed_list)
        self.assertFalse(is_prime)

    def test_give_13_17_19_is_prime(self):
        prime_list = [13, 17, 19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_10_is_not_prime(self):
        not_prime_list = [10]
        is_prime = is_prime_list(not_prime_list)
        self.assertFalse(is_prime)

# if __name__ == '__main__':
#     unittest.main()
