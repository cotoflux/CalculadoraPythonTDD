import unittest
from Calculadora import Calculadora

class MyTestCase(unittest.TestCase):
    def test_inicializaValor(self):
        valorEsperado = 0
        calculadora = Calculadora
        valorClasse = calculadora.valor
        self.assertEqual(valorEsperado, valorClasse)



    def test_sumaTotal(self):
        calculadora = Calculadora
        numero1 = 2
        numero2 = 1
        totalSumaExpected = numero1 + numero2;
        totalSumaClasse = calculadora.suma(self, numero1, numero2)
        self.assertEqual(totalSumaExpected, totalSumaClasse)


if __name__ == '__main__':
    unittest.main()
