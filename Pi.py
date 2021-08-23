from fractions import Fraction

from decimal import *

getcontext().prec = 1000

def arctan(x, p) :
    y = Fraction(0,1)
    k = 0
    for j in range(0, p):
        k = 2*j+ 1
        y = y + ((-1)**j)*Fraction(x**k, k)
    return y


a = Fraction(1,2)
b = Fraction(1,3)

p = 2000

a = Fraction(4,1)*arctan(a, p)

b = Fraction(4,1)*arctan (b, p)
pi = a + b

 
piString = str(Decimal(pi.numerator)/pi.denominator)
decDig =""



for j in range (962,972):
    decDig += piString[j]
print(decDig)