import unittest
from Calculate import Calculate

class TestCalculate (unittest.TestCase):
    def setUp (self):
        self.calc = Calculate()

    def regra_0_base_soma_inteiros (self):
        self.assertEqual (4, self.calc.add(2,2))

    def regra_1_levanta_erro_strings (self):
        self.assertRaises (TypeError, self.calc.add, "Hello","World")

    #def regra_2_levanta_erro_floats (self):
        #self.assertRaises (TypeError, self.calc.add, 3.12, 3.12)

if __name__ == '__main__':
    unittest.main()
