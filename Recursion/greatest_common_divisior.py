# gcd(a,b) = gcd (b,a mod b)
# gcd(a,0) = a

def gcd_of_two_number(a,b):
    assert int(a) == a and int(b) ==b, "The Numbers must be Integers only !!"
    if a <0 :
        a = -1*a
    if b <0:
        b = -1*b
    if b==0:
        return a
    else :
        return gcd_of_two_number(b,a%b)



print(gcd_of_two_number(-12,4))
