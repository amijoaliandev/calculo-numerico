def newton_raphson(f, df, x0, tolerancia=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Derivada cero.")
            return None
        x1 = x - fx / dfx
        if abs(x1 - x) < tolerancia:
            return x1, i + 1
        x = x1
    return None