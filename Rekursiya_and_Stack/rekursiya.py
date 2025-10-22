def recursion_factorial(n):
    if n < 0:
        raise ValueError("Manfiy son kiritib bo'lmaydi!")
    
    if n == 0:
        return 1
    
    return n * recursion_factorial(n - 1)
