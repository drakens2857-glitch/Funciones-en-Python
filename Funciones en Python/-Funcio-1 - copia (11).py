palabras = ["python", "es", "un", "lenguaje", "genial", "y", "poderoso"]

def longitud(palabra):
    return len(palabra)

ordenadas1 = sorted(palabras, key=longitud)
print("Con función normal:", ordenadas1)

ordenadas2 = sorted(palabras, key=lambda p: len(p))
print("Con lambda:", ordenadas2)
