import pylab as pl
import numpy as np
import scipy as sp
import scipy.integrate as spi
import matplotlib.pyplot as plt

G=6.67e-11 #Gravitational Constant
M=6.4e23 #Mass of Mars
m=260 #Mass of Satellite
r=3.4e6 #Radius of Mars
mv=2.41e4 #Velocity of Mars

def f(x,t):
    xx=x[0] #Displacement in x-direction
    vx=x[1] #Velocity in x-direction
    yy=x[2] #Displacement in y-direction
    vy=x[3] #Velocity in y-direction
  
    ax=-(G*M*xx)/(xx**2+yy**2)**1.5 #Acceleration in x-direction
    ay=-(G*M*yy)/(xx**2+yy**2)**1.5 #Acceleration in y-direction
    d=(xx**2+yy**2)**0.5 #Distance between the centres of mass of the satellite and Mars
 
   
    if d>r:
        return [vx+mv,ax,vy,ay] #Returns required values
        
    else:
        print ("Collision occured at the distance;", d)
        return [0,0,0,0]

'''to see One particular Path
xx0=[10*r, 'velocity in x direction', 10*r,'velocity in y directio ] #The satellite escapes in front of Mars
soln=spi.odeint(f,xx0,t)
x=soln[:,0] #x-displacement
xv=soln[:,1] #x-velocity
y=soln[:,2] #y-displacement
yv=soln[:,3] #y-velocity

pl.figure(1)
pl.plot(mv*t,t,'o',color='orange')
pl.plot(x,y,'-b')

pl.axis([-1e8,1e8,-4e7, 4e7])
pl.xlabel('x displacement ($m$)')
pl.ylabel('y displacement ($m$)')
pl.legend(['Path of Mars','Path of the satellite'])
pl.grid()

'''

t=sp.linspace(0,1000,100000) #Range of time and interval

iv=sp.linspace(-2.2e2,-2.6e2,10) #Range of initial velocity of satellite in x-direction

for v in iv:
    xx0=[10*r, v, 10*r, -2000] #Initial condition for the satellite that escapes in front of Mars
    soln=spi.odeint(f,xx0,t)
    x=soln[:,0] #x-displacement
    xv=soln[:,1] #x-velocity
    y=soln[:,2] #y-displacement
    yv=soln[:,3] #y-velocity

    vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
    
    ke=0.5*m*(vs**2) #Kinetic Energy
    gpe=-G*M*m/(x**2+y**2)**0.5 #Gravitational Potential Energy
    te=ke+gpe #Total Energy, to see whether energy conserved

    pl.figure(1)
    pl.plot(t,ke,'r')
    pl.plot(t,gpe,'g')
    pl.plot(t,te,'b')
    pl.legend(['KE','GPE', 'TE'])
    pl.axis([0,1e6,-3e7,3e7])
    pl.xlabel('time($s$)')
    pl.ylabel('Energy($J$)')
    pl.title("Energy Variation of Satellite")
  
    #print(sorted(vs)) 

    pl.figure(3)
    pl.plot(mv*t,t,'o',color='orange') #To trace the motion of Mars
    pl.plot(x,y,'-b')
    
    pl.axis([-1e8,1e8,-4e7, 4e7])
    pl.xlabel('x displacement ($m$)')
    pl.ylabel('y displacement ($m$)')
    pl.legend(['Path of Mars','Path of the satellite'],loc='lower left')
    pl.title('Path of the satellite escaping in front of Mars')

pl.show()
