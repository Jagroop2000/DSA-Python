# Function that Solve Factorial Uing Recursion 
def factorial(n):
    assert n>=0 and int(n) == n, "The Number must be positive Integer only !"
    if n in [0,1]:
        return 1
    return n * factorial(n-1)


print(factorial(4))