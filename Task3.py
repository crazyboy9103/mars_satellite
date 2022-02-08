import pylab as pl
import numpy as np
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt

G=6.67e-11 #Gravitational Constant
M=6.4e23 #Mass of Mars
m=260 #Mass of Satellite
r=3.4e6 #Radius of Mars
mv=2410 #Velocity of Mars
def f(x,t):
    xx=x[0] #Displacement in x-direction
    vx=x[1] #Velocity in x-direction
    yy=x[2] #Displacement in y-direction
    vy=x[3] #Velocity in y-direction
  
    ax=-(G*M*xx)/(xx**2+yy**2)**1.5 #Acceleration in x-direction
    ay=-(G*M*yy)/(xx**2+yy**2)**1.5 #Acceleration in y-direction
    d=(xx**2+yy**2)**0.5 #Distance between the centres of mass of the satellite and Mars
    
    
    return [vx,ax,vy,ay] #Returns required values


  
t=sp.linspace(0,1000000,1000) 

xx0=[7*r, -1200, 3*r, 1200] #Elongated path

soln=spi.odeint(f,xx0,t)
x=soln[:,0] #x-displacement
xv=soln[:,1] #x-velocity
y=soln[:,2] #y-displacement
yv=soln[:,3] #y-velocity

vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
ke=0.5*m*(vs**2)
gpe=-G*M*m/(x**2+y**2)**0.5
te=ke+gpe

pl.figure(1,)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($t$)')
pl.ylabel('Energy($J$)')
pl.title('Energy Variation of Elongated Path')
pl.legend(['KE','GPE', 'TE'])
pl.grid()

        
xx1=[7*r, -850, 3*r, 850] #Almost circular path
soln1=spi.odeint(f,xx1,t)
x=soln1[:,0] #x-displacement
xv=soln1[:,1] #x-velocity
y=soln1[:,2] #y-displacement
yv=soln1[:,3] #y-velocity

vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
ke=0.5*m*(vs**2)
gpe=-G*M*m/(x**2+y**2)**0.5
te=ke+gpe

pl.figure(2,)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($t$)')
pl.ylabel('Energy($J$)')
pl.title('Energy Variation of Circular Path')
pl.legend(['KE','GPE', 'TE'])
pl.grid()

xx2=[7*r, -1500, 3*r, 1500] #The satellite escapes
soln2=spi.odeint(f,xx2,t)
x=soln2[:,0] #x-displacement
xv=soln2[:,1] #x-velocity
y=soln2[:,2] #y-displacement
yv=soln2[:,3] #y-velocity

vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
ke=0.5*m*(vs**2)
gpe=-G*M*m/(x**2+y**2)**0.5
te=ke+gpe

pl.figure(3)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($t$)')
pl.ylabel('Energy($J$)')
pl.title("Energy Variation of Escaped satellite")
pl.axis([0,0.1e7,-1e9,1e9])
pl.legend(['KE','GPE', 'TE'])
pl.grid()

    
pl.show()
