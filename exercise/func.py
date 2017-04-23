def remainder(a, b):
    q = a // b
    r  = a - q * b
    return r

def devide(a , b):
    q = a // b
    r = a - q*b
    return (q, r)
qutient, remainder = devide(1456, 33)
print (qutient, remainder)
