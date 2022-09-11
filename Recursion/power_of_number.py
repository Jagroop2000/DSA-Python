def power_of_number(n,p):
    assert p>=0 and int(p) == p,'The Exponenet must be positive integer '
    if p ==0:
        return 1
    if p ==1 :
        return n
    else:  
        return n * power_of_number(n,p-1)


print(power_of_number(-5.5,5))