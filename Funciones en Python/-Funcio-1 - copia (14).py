def crear_contador():
    n = 0
    def incrementar():
        nonlocal n
        n += 1
        return n
    return incrementar

contador1 = crear_contador()
contador2 = crear_contador()

print("Contador 1:", contador1())
print("Contador 1:", contador1())
print("Contador 1:", contador1())
print("Contador 2:", contador2())
print("Contador 2:", contador2())
