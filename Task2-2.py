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
       
    if vs>=ev:
        return [vx,ax,vy,ay] #If the velocity of satellite is bigger than escape velocity of Mars
    else:
        return [0,0,0,0] #Returns nothing



ad=[] #Angular deviation

iv=sp.linspace(0,100000,1000)
t=sp.linspace(0,100000,1000)

for i in iv:    #Initial Velocity in the list
    xx1=[7*r, -i, 3*r, i] #Initial conditions as required
    soln1=spi.odeint(f,xx1,t) 
    
    v1=soln1[:,1] #x-velocity
    v2=soln1[:,3] #y-velocity (as only velocity components required to calculate angular deviation)

    theta=sp.arctan(v1[-1]/v2[-1]) #Define the angle
    
    ad.append(theta)
    #print (sorted(ad))
        
pl.figure(2,)
pl.title("The angular deviation of the satellite")
pl.axis([0, 6000, -2, 2])
pl.plot(iv, ad,'-b') #Both are lists
pl.xlabel("Initial Velocity ($ms^{-1}$)")
pl.ylabel("Angular Deviation ($rad$)")
pl.grid()


pl.show()
