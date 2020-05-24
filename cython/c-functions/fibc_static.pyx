def fibonacci_cs(int n):
    if n < 2:
        return n
    return fibonacci_cs(n-2) + fibonacci_cs(n-1)
