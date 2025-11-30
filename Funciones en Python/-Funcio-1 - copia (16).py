def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))
print("Factorial de 7:", factorial(7))
print("Factorial de 3:", factorial(3))
