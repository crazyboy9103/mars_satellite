import pylab as pl
import numpy as np
import scipy as sp
import scipy.integrate as spi

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
  ev=(2*G*M/d)**0.5 #Escape velocity of the satellite
  vs=(vx**2+vy**2)**0.5 #Magnitude of velocity of the satellite
  if d<=r:
      if vs<=ev:
          return [0,0,0,0] #If the velocity of the satellite is smaller than the escape velocity
      
  else:
      return [vx,ax,vy,ay] #Return the values

t=sp.linspace(0.,1000000.,1000)

iv=sp.linspace(0,100000,1000)
for v in iv:
    xx0=[7*r, -v, 3*r, v] #Initial conditions as required
    soln=spi.odeint(f,xx0,t) 
    x=soln[:,0] #x-displacement
    vx=soln[:,1] #x-velocity
    y=soln[:,2] #y-displacement
    vy=soln[:,3] #y-velocity
    
    circle=pl.Circle((0,0),r,fc='orange')
    fig = pl.gcf()
    fig.gca().add_artist(circle) #Representation of Mars
    
    pl.figure(1,)
    pl.title("The path of the satellite when it is captured")
    pl.axis([-4e7, 4e7, -5e7, 3e7])
    pl.plot(x,y)
    pl.xlabel("x-displacement ($m$)")
    pl.ylabel("y-displacement ($m$)")

pl.show()
