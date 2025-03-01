import unittest
from Calculo import Calculo

class TestCalculo (unittest.TestCase):
    def setUp (self):
        self.calculo = Calculo()
    
    def test_somar_com_retorno_correto (self):
        self.assertEqual (4, self.calculo.somar(3,1))

    def test_somar_com_verificacao_errada (self):
        self.assertEqual (5, self.calculo.somar(3,1))

    def test_somar_com_excecao_no_teste (self):
        print ("Ola --->")
        self.assertRaises (TypeError, self.calculo.somar("Hello ","World"))

if __name__ == '__main__':#pragma:no cover
    unittest.main()
