def biseccion(f, a, b, tolerancia=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de bisección no es aplicable.")
        return None
    for i in range(max_iter):
        m = (a + b) / 2
        if abs(f(m)) < tolerancia or (b - a) / 2 < tolerancia:
            return m, i + 1
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return None