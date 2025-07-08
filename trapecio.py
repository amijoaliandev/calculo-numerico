def trapecio(f, a, b, n):
    """
    Aproximación de la integral definida de f(x) usando el método del trapecio.

    Parámetros:
    - f: función a integrar
    - a: límite inferior
    - b: límite superior
    - n: número de trapecios

    Retorna:
    - área aproximada bajo la curva
    """
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)

    return (h / 2) * suma