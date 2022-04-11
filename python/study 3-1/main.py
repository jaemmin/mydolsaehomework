def factorial(x):
    result = 1
    for i in range(x+1):
        result *= i
    return result
print(factorial(3))