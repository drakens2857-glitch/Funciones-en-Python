def fibonacci_lento(n):
    if n < 2:
        return n
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)

print(fibonacci_lento(10))

