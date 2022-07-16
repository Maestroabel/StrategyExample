import unittest
from calc import Calc

class TestStringMethods(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(True, True)
        
    def test_sumar(self):
        calc = Calc
        result = calc.sumar(3,2)
        self.assertEqual(5, result)
        
    def test_restar(self):
        # 3 - 2 = 1
        calc = Calc
        result = calc.restar(3,2)
        self.assertEqual(1, result)
        
if __name__ == '__main__':
    unittest.main()        