def sum_of_digits(n):
    assert n>=0 , 'The number must be positive integer only'
    if n==0 :
        return 0
    else :
        return int(n%10) + int(sum_of_digits(n/10))


print(sum_of_digits(124))