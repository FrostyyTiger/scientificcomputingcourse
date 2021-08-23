from numpy import matrix as mat
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import time as time




def dotp(a,b):
    """
    Input: Two 1x3 Matrixes
    Output: Scalar, dotproduct of the two inputs
    """
    return(float(a * b.T))


def rotx(x, phi):
    """
    Input: x should be a 3x1 Matrix Object, phi a float between -pi and pi
    """
    c = np.cos(phi)
    s = np.sin(phi)
    rx = mat([[1, 0, 0], 
              [0, c, s], 
              [0, -s, c]])
    b = x*rx
    return b

def rotz(x, phi):
    """
    Input: x should be a 3x1 Matrix Object, phi a float between -pi and pi
    """
    c = np.cos(phi)
    s = np.sin(phi)
    rx = mat([[c, s, 0], 
              [-s, c, 0], 
              [0, 0, 1]])
    b = x*rx
    return b
    
        
def roty(x, phi):
    """
    Input: x should be a 3x1 Matrix Object, phi a float between -pi and pi
    """
    c = np.cos(phi)
    s = np.sin(phi)
    rx = mat([[c, 0, -s], 
              [-s, c, 0], 
              [0, 0, 1]])
    b = x*rx
    return b
    

def dasun(t):
    ex = mat([1,0,0])
    winkel = ((2*3.1415926535897932384626433832795028841971693)/365)*t
    s = rotz(ex, winkel)
    return s


def dalocation(late, long, dayofyear, timeofday):
    pi = 3.1415926535897932384626433832795028841971693
    ex = mat([1,0,0])
    
    later = (-pi/180)*late
    longer = (pi/180)*long
    dayer = (1/24)*2*pi
    yearer = (1/365)*2*pi
    inclphi = ((2*pi)/365)*dayofyear
    heyo = (23.5*pi)/180
    incl = np.sin(inclphi)*heyo
    
    pet = roty(ex, later)
    
    peter = rotz(pet, longer+dayer+yearer)
    
    peterer = rotx(peter, incl)
    return peterer
    
    
    
    

def intensity(timeofday, dayofyear, lat, long):
    
    esun = dasun(dayofyear)
    eloc = dalocation(lat, long, dayofyear, timeofday)
    
    i = dotp(esun, eloc)
    return i

def imap(N, tod, doy):
    pi = 3.1415926535897932384626433832795028841971693
    a = np.zeros((N,N))
    
    for i in range(N):
        long = -180 + (360/N)*i
        for j in range(N):
            lat = (-90)+(180/N)*j
            b = intensity(tod, doy, long, lat)
            a[i][j] = b
    return a
    
            






fig = plt.figure()
axes = fig.add_subplot(1,1,1)
img = imread('map.jpg')

t = 20

levels = np.linspace(-1, 1, 15)
N = 15
doy = 1



while t<24:
    axes.clear()
    axes.imshow(img)
    
    z = imap(N, t, doy)
    y = np.linspace(0, 302, N)
    x = np.linspace(0, 603, N)
    
    axes.contourf(x, y, z, levels, cmap='hot', alpha=0.8)
    t = t+0.1
    plt.pause(0.01)