import unittest

from client import getRatio


class TestGetRation(unittest.TestCase):
    def test_ration_is_correctly_calculated(self):
        self.assertEqual(getRatio (10, 5), 2)
        self.assertEqual(getRatio (5, 10), 0.5)
        self.assertEqual(getRatio (10, 10), 1)
        
    def test_ration_is_none_when_divisor_is_zero(self):
        self.assertIsNone(getRatio (10, 0))
        self.assertIsNone(getRatio (0, 0))
    
    def test_ratio_of_zero_and_nonezero_is_zero(self):
        self.assertEqual(getRatio (0, 10), 0)
        self.assertEqual(getRatio (0, 5), 0)
        

if __name__ == '__main__':
    unittest.main()