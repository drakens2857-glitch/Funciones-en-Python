def mostrar_datos(**datos):
    print("Información recibida:")
    for clave, valor in datos.items():
        print(f" {clave}: {valor}")

mostrar_datos(nombre="Ana", edad=20, ciudad="Bogotá")
print()
mostrar_datos(producto="Laptop", precio=1500000, marca="Dell", año=2023)
