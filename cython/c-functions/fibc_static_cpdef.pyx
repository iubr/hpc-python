cpdef int fibonacci_csdef(int n):
    if n < 2:
        return n
    return fibonacci_csdef(n-2) + fibonacci_csdef(n-1)
