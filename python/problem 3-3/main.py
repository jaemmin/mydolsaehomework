def func(x):
    y = pow(x, pow(x, pow(x, x)))
    return y

def dif(x):
    y = (func(x+h)-func(x))/h
    return y


h = 1e-10

print(dif(2))