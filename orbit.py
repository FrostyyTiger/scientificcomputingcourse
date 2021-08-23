#Orbit
#Imports
from numpy import *
import matplotlib.pyplot as mat


def x_co(e_g):
    """
    This function returns the x-coordinate of the Orbit depending on eE
    """
    return 17.8*(cos(e_g)-0.967)

def y_co(e_g):
    """
    This function returns the y-corrdinate of the Orbit depending on E
    """
    a = (1-0.967**2)**(1/2)
    b = sin(e_g)
    return 17.8*(a*b)

def f(m,e_g):
    """
    returns the function of m,e and E
    """
    return e_g-0.967*sin(e_g)-m

def df(m,e_g):
    """
    returns der derivated function of m,e and E
    """
    return 1-0.967*cos(e_g)

def newson(m,e_g):
    """
    calculate the next step with the newton raphson thing
    """
    mf = f(m,e_g)
    mdf = df(m,e_g)
    a = e_g - (mf/mdf)
    return a

def calce(m):
    """
    This function returns E for a specific m
    such that the coordinates can be calculated
    """
    E=4
    old = [5]
    checker = True
    while f(m,E) != 0.0 and checker == True:
        E = newson(m, E)
        if E in old:
            """
            This if detects if the newton-raphson methods starts going in circles
            if it does it stops the while-loop
            """
            checker = False
            #print("Looping error try different E starting Value")
        old.append(E)        
        
    return E
#The following lines calculates all the x and y values of the Orbit
n = 200
x_values = []
y_values = []
for i in range(n):
    m = ((2*pi)/n)*i
    E=calce(m)
    x_values.append(x_co(E))
    y_values.append(y_co(E))


mat.plot(x_values,y_values,'.') #create the plot
mat.show() #show the plot
