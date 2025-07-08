def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función.

    Parámetros:
    - f: función original
    - df: derivada de la función
    - x0: valor inicial
    - tolerancia: precisión deseada
    - max_iter: número máximo de iteraciones

    Retorna:
    - (raíz, iteraciones) si tiene éxito
    - None si no converge
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivada cero. No se puede continuar.")
            return None

        x1 = x - fx / dfx

        if abs(x1 - x) < tolerancia:
            return x1, i + 1

        x = x1

    print("No se encontró una raíz con la precisión deseada.")
    return None