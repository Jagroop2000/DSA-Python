# Function For Fibonacci Number 

def fibonacci(n):
    assert n>=0 and int(n) == n ,"Input must be a Positive Number "
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))

# 5 ->