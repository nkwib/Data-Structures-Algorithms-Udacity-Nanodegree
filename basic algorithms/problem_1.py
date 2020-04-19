def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        if number < 0 :
            return 'complex numbers not supported'
        elif number >= 0:
            return int(number**(1/2))
    except:
        return 'data type not supported'



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(37)) else "Fail")
print ("Pass" if  (9 == sqrt(88)) else "Fail")
print ("Pass" if  (16 == sqrt(256)) else "Fail")
print (sqrt(-27))
print (sqrt({}))
print (sqrt('Hello'))