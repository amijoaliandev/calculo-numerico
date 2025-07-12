import unittest
from riemann import riemann

class TestRiemann(unittest.TestCase):
    def test_area_x2(self):
        f = lambda x: x**2
        resultado = riemann(f, 0, 2, 1000)
        self.assertAlmostEqual(resultado, 8/3, places=2)