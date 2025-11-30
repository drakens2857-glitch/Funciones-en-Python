def funcion(a, b, /, c, *, d, e):
    return a + b + c + d + e

print(funcion(1, 2, 3, d=4, e=5))
print(funcion(1, 2, c=3, d=4, e=5))
