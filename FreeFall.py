import numpy as np
import matplotlib.pyplot as plt




def abl(x):
    """
    This function calculates the derivate for free fall experiments
    
    Params:
        x: list with length four, the list that should be derivated
    Outputs:
        y: list with length four, derivation of x
    """
    y = [0,0,0,0]
    y[0] = x[2]
    y[1] = x[3]
    y[2] = 0
    y[3] = -1
    return y


def euler(f, start, end, N):
    """
    This function calculates the path of an object in free fall approximately using the euler method
    
    Params:
        f: Initial conditions with (x,y,vx,vy)
        start: the beginning of time
        stop: the end of our times
        N: how many steps should be calculated
    Outputs:
        x: List with length N+1, x[i] corresponds to y[i], all x coordinates
        y: List with length N+2, y[i] is a function of x[i], all y coordinates
    """
    x = []
    y = []
    deltat = (abs(start-end)/N)
    for i in range(N):
        df = abl(f)
        for i in range(4):
            f[i]=f[i]+df[i]*deltat
        x.append(f[0])
        y.append(f[1])
    return x,y


def kutta(f, start, end, N):
    """
    This function calculates the path of an object in free fall 
    approximately using the runge-kutta-2 method
    
    Params:
        f: Initial conditions with (x,y,vx,vy)
        start: the beginning of time
        stop: the end of our times
        N: how many steps should be calculated
    Outputs:
        x: List with length N+1, x[i] corresponds to y[i], all x coordinates
        y: List with length N+2, y[i] is a function of x[i], all y coordinates
    """
    x = []
    y = []
    deltat = (abs(start-end)/N)
    
    for i in range(N):
        df = abl(f)
        zw = [0,0,0,0]
        for i in range(4):
            zw[i] = f[i]+deltat*df[i]
        ddf = abl(zw)
        for i in range(4):
            f[i]=f[i]+ (1/2)*deltat*(df[i]+ddf[i])
        x.append(f[0])
        y.append(f[1])
    return x,y

#Uncomment the following block to see the results of Excercise 1

"""
a=[0, 0, 0.1, 10]
b = euler(a, 0, 20, 50)

a=[0, 0, 0.1, 10] 
c = kutta(a, 0, 20, 50)

x1 = b[0]
y1 = b[1]
x2 = c[0]
y2 = c[1]


plt.plot(x1, y1, 'r.')
plt.plot(x2, y2, 'b.')
plt.show()
"""

def abl2(x, omega, t):
    """
    This function calculates the derivate for the cyclotron experiment
    
    Params:
        x: list with length four, the list that should be derivated
    Outputs:
        y: list with length four, derivation of x
    """
    y = [0,0,0,0]
    y[0] = x[2]
    y[1] = x[3]
    y[2] = 2*x[3]
    y[3] = -2*x[2]*np.cos(omega*t)
    return y

def euler2(f, start, end, N, omega):
    """
    This function calculates the path of an object in free fall approximately using the euler method
    
    Params:
        f: Initial conditions with (x,y,vx,vy)
        start: the beginning of time
        stop: the end of our times
        N: how many steps should be calculated
        omega: the angular velocity
    Outputs:
        x: List with length N+1, x[i] corresponds to y[i], all x coordinates
        y: List with length N+2, y[i] is a function of x[i], all y coordinates
    """
    x = []
    y = []
    deltat = (abs(start-end)/N)
    for i in range(N):
        df = abl2(f, omega, (deltat*i))
        for i in range(4):
            f[i]=f[i]+df[i]*deltat
        x.append(f[0])
        y.append(f[1])
    return x,y

def kutta2(f, start, end, N, omega):
    """
    This function calculates the path of an object in free fall 
    approximately using the runge-kutta-2 method
    
    Params:
        f: Initial conditions with (x,y,vx,vy)
        start: the beginning of time
        stop: the end of our times
        N: how many steps should be calculated
        omega: The angular velocity
    Outputs:
        x: List with length N+1, x[i] corresponds to y[i], all x coordinates
        y: List with length N+2, y[i] is a function of x[i], all y coordinates
    """
    x = []
    y = []
    deltat = (abs(start-end)/N)
    
    for i in range(N):
        df = abl2(f, omega, deltat*i)
        zw = [0,0,0,0]
        for i in range(4):
            zw[i] = f[i]+deltat*df[i]
        ddf = abl2(zw, omega, deltat*i)
        for i in range(4):
            f[i]=f[i]+ (1/2)*deltat*(df[i]+ddf[i])
        x.append(f[0])
        y.append(f[1])
    return x,y

#Uncomment the following Block to see the results from excercise two


omega = 0


k = [0, 1+(1/(4-omega**2)), 2+(2/(4-omega**2)), 0]
d = euler2(k, 0, 10, 500000, omega)
x3 = d[0]
y3 = d[1]

plt.figure(2, figsize=(5,5))
plt.plot(x3, y3, 'g-')


k = [0, 1+(1/(4-omega**2)), 2+(2/(4-omega**2)), 0]
e = kutta2(k, 0, 10, 5000, omega)
x4 = e[0]
y4 = e[1]


plt.plot(x4, y4, 'r-')
plt.show()
