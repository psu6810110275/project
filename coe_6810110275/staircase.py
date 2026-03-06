def staircase(n, pattern):
    if n <= 0 or n > 30:
        return ""
    
    result = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        chars = pattern * i
        result.append(spaces + chars)
        
    return "\n".join(result)
