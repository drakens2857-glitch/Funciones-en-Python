def area_rectangulo(base: float, altura: float) -> float:
    if base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser positivos")
    return base * altura

print(area_rectangulo(3, 4))
print(area_rectangulo(5.5, 2.0))
