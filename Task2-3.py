import pylab as pl
import numpy as np
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt

G=6.67e-11 #Gravitational Constant
M=6.4e23 #Mass of Mars
m=260 #Mass of Satellite
r=3.4e6 #Radius of Mars

def f(x,t):
    xx=x[0] #Displacement in x-direction
    vx=x[1] #Velocity in x-direction
    yy=x[2] #Displacement in y-direction
    vy=x[3] #Velocity in y-direction
  
    ax=-(G*M*xx)/(xx**2+yy**2)**1.5 #Acceleration in x-direction
    ay=-(G*M*yy)/(xx**2+yy**2)**1.5 #Acceleration in y-direction
    d=(xx**2+yy**2)**0.5 #Distance between the centres of mass of the satellite and Mars
    ev=(2*G*M/d)**0.5 #Escape velocity of Mars
    vs=(vx**2+vy**2)**0.5 #Magnitude of velocity of the satellite
       
    if vs>ev:
        return [0,0,0,0] #If the velocity of satellite is bigger than escape velocity of Mars
    else:
        return [vx,ax,vy,ay] #Returns values



iv=sp.linspace(0,10000,1000)
t=sp.linspace(0,10000,1000)
min_seps = []
xs =[]
ys =[]

for v in iv:
    xx0=[7*r, -v, 3*r, v] #Initial conditions as required
    soln=spi.odeint(f,xx0,t)
    
    x=soln[:,0] #x-displacement
    y=soln[:,2] #y-displacement
    
    xs.append(x)
    ys.append(y)
    
    
    min_sep =(np.min(x)**2+np.min(y)**2)**0.5
    min_seps.append(min_sep)

pl.figure(1,)
pl.gca().add_artist(pl.Circle((0,0),r,fc='orange')) 
pl.title("The satellite")
pl.xlabel("x displacement ($m$)")
pl.ylabel("y displacement($m$)")

for x, y in zip(xs, ys):
    pl.plot(x, y,'-b')

pl.figure(2)
pl.title("MInimum seperation")
pl.plot(iv, min_seps)
pl.xlabel("initial velocity ($ms^{-1}$)")
pl.ylabel("minimum seperation ($m$)")

  
        
pl.show()
