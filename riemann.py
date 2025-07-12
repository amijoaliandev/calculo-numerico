def riemann(f, a, b, n):
    ancho = (b - a) / n
    suma = 0
    for i in range(n):
        xi = a + i * ancho
        suma += f(xi)
    return suma * ancho