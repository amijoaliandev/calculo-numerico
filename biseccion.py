def biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    """
    Método de bisección para encontrar raíces de una función continua en [a, b].

    Parámetros:
    - f: función que recibe un valor x y devuelve f(x)
    - a: extremo izquierdo del intervalo
    - b: extremo derecho del intervalo
    - tolerancia: error mínimo deseado
    - max_iter: número máximo de iteraciones permitidas

    Retorna:
    - (raíz, iteraciones) si se encuentra una raíz
    - None si no se encuentra una raíz
    """
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable: f(a) y f(b) no tienen signos opuestos.")
        return None

    for i in range(max_iter):
        m = (a + b) / 2
        fm = f(m)

        if abs(fm) < tolerancia or (b - a) / 2 < tolerancia:
            return m, i + 1

        if f(a) * fm < 0:
            b = m
        else:
            a = m

    print("No se encontró una raíz con la precisión deseada.")
    return None