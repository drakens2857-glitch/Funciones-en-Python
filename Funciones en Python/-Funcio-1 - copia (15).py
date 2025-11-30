from functools import wraps

def repetir(veces=1):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = None
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(veces=3)
def saludar(nombre):
    print(f"¡Hola {nombre}!")

@repetir(veces=5)
def despedir(nombre):
    print(f"¡Adiós {nombre}!")

saludar("Ana")
print()
despedir("Luis")
