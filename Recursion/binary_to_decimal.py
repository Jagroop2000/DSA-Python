def convert_Dec_to_binary(n):

    # unintentional case
    assert int(n)==n ,"Parameter must be an Integer Only"

    if  n==0:
        return 0
    else :
        return (n%2)+ 10*convert_Dec_to_binary(int(n/2))



print(convert_Dec_to_binary(13))