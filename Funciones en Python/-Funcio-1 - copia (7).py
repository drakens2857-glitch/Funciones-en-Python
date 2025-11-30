def sumar(*numeros):
    print("Recibí estos números:", numeros)
    return sum(numeros)

print("Suma de 2 números:", sumar(1, 2))
print("Suma de 5 números:", sumar(1, 2, 3, 4, 5))
print("Suma de 8 números:", sumar(10, 20, 30, 40, 50, 60, 70, 80))
