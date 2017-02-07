import unittest

class TestPrimeNumbers(unittest.TestCase):
    def test_zero_prime(self):
        self.assertFalse(is_prime(0), msg='Zero is not a prime number')
    def test_one_prime(self):
        self.assertFalse(is_prime(1), msg='One is not a prime number')
    def test_two_prime(self):
        self.assertEqual(is_prime(2), 2)
    def test_eleven_prime(self):
        self.assertEqual(is_prime(11), 11)
    def test_for_floatingNum(self):
        self.assertFalse(is_prime(3.9),)
    def test_negative(self):
        self.assertFalse(is_prime(-7), msg = 'You have entered a negative number')
        
if __name__ == '__main__':
    unittest.main()




    