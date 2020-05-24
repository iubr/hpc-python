def fibonacci_c(n):
    if n < 2:
        return n
    return fibonacci_c(n-2) + fibonacci_c(n-1)
