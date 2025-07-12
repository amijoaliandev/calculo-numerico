def trapecio(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)
    return (h / 2) * suma