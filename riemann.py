def riemann(f, a, b, n):
    """
    Aproximación de la integral definida de f(x) usando sumas de Riemann (rectángulos).

    Parámetros:
    - f: función a integrar
    - a: límite inferior
    - b: límite superior
    - n: número de rectángulos

    Retorna:
    - área aproximada bajo la curva
    """
    ancho = (b - a) / n
    suma = 0
    for i in range(n):
        xi = a + i * ancho
        suma += f(xi)
    return suma * ancho