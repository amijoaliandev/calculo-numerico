import unittest
from biseccion import biseccion

class TestBiseccion(unittest.TestCase):
    def test_con_raiz(self):
        f = lambda x: x**2 - 4
        resultado = biseccion(f, 1, 3)
        self.assertIsNotNone(resultado)
        raiz, _ = resultado
        self.assertAlmostEqual(raiz, 2.0, places=4)

    def test_sin_raiz(self):
        f = lambda x: x**2 + 4
        resultado = biseccion(f, -2, 2)
        self.assertIsNone(resultado)