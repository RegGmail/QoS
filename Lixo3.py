import unittest
from Calculate import Calculate

class TestCalculate (unittest.TestCase):
    def setUp (self):
        self.calc = Calculate()

    def test_add_method_returns_corret_result (self):
        self.assertEqual (4, self.calc.add(2,2))
        self.assertEqual (3, self.calc.add (4, -2))
        self.assertEqual (-8, self.calc.add (-16, 8))

    def test_add_method_raises_typerror_if_not_ints (self):
        self.assertRaises (TypeError, self.calc.add, "Hello","World")

if __name__ == '__main__':
    unittest.main()

