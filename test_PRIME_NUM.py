import unittest
from prime_num import is_prime

class TestPrimeNumbers(unittest.TestCase):
    def test_zero_prime(self):
        self.assertFalse(is_prime(0), msg='Zero is not a prime number')
    def test_one_prime(self):
        self.assertFalse(is_prime(1), msg='One is not a prime number')
    def test_two_prime(self):
        self.assertEqual(is_prime(2), 2)
    def test_eleven_prime(self):
        self.assertEqual(is_prime(11), 11)
    def test_negative(self):
        for item in range(-1, -10, -1):
            self.assertFalse(is_prime(item), msg = '{}You have entered a negative number'.format(item))

if __name__ == '__main__':
    unittest.main()




    
