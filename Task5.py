import pylab as pl
import numpy as np
import scipy as sp
import scipy.integrate as spi

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
  
  if d<r: 
      return [0,0,0,0] #If the satellite collides with Mars
      
      
  else:
      return [vx,ax,vy,ay] #Return the values
      

  if (ax**2+ay**2)**0.5==0:
      print (vx,vy)

t=sp.linspace(0,1000000,1000) 
iv=sp.linspace(0,100000,1000)
#--------------------------------------------------------------------------#
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
#------------------------------------------Task 2-1-------------------------#
ad=[] #Angular deviation

for i in iv:    #Initial Velocity in the list
    xx1=[7*r, -i, 3*r, i] #Initial conditions as required
    soln1=spi.odeint(f,xx1,t) 
    
    v1=soln1[:,1] #x-velocity
    v2=soln1[:,3] #y-velocity (as only velocity components required to calculate angular deviation)

    theta=sp.arctan(v1[-1]/v2[-1]) #Define the angle
    
    ad.append(theta)
   
        
pl.figure(2,)
pl.title("The angular deviation of the satellite")
pl.axis([0, 6000, -2, 2])
pl.plot(iv, ad,'-b') #Both are lists
pl.xlabel("Initial Velocity ($ms^{-1}$)")
pl.ylabel("Angular Deviation ($rad$)")
pl.grid()


pl.show()
#-----------------------------------------Task3-----------------------------#

xx2=[7*r, -1200, 3*r, 1200] #Elongated path

soln2=spi.odeint(f,xx2,t)
x=soln2[:,0] #x-displacement
xv=soln2[:,1] #x-velocity
y=soln2[:,2] #y-displacement
yv=soln2[:,3] #y-velocity

vs=(xv**2+yv**2)**0.5 #Magnitude of Velocity of the Satellite
ke=0.5*m*(vs**2) #Kinetic Energy
gpe=-G*M*m/(x**2+y**2)**0.5 #Gravitational Potential Energy
te=ke+gpe #Total Energy
#---------------------------------------------------------------------------#
pl.figure(3,)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($s$)')
pl.ylabel('Energy($J$)')
pl.title('Energy Variation of Elongated Path')
pl.legend(['KE','GPE', 'TE'])
pl.grid() 

xx3=[7*r, -850, 3*r, 850] #Almost circular path
soln3=spi.odeint(f,xx3,t) #Solve 1st order ODE
x=soln3[:,0] #x-displacement
xv=soln3[:,1] #x-velocity
y=soln3[:,2] #y-displacement
yv=soln3[:,3] #y-velocity

vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
ke=0.5*m*(vs**2) #Kinetic Energy
gpe=-G*M*m/(x**2+y**2)**0.5 #Gravitational Potential Energy
te=ke+gpe #Total Energy
#---------------------------------------------------------------------------#
pl.figure(4,)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($s$)')
pl.ylabel('Energy($J$)')
pl.title('Energy Variation of Circular Path')
pl.legend(['KE','GPE', 'TE'])
pl.grid()

xx4=[7*r, -1500, 3*r, 1500] #The satellite escapes
soln4=spi.odeint(f,xx4,t)
x=soln4[:,0] #x-displacement
xv=soln4[:,1] #x-velocity
y=soln4[:,2] #y-displacement
yv=soln4[:,3] #y-velocity


vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
ke=0.5*m*(vs**2)
gpe=-G*M*m/(x**2+y**2)**0.5
te=ke+gpe
#---------------------------------------------------------------------------#
pl.figure(5)
pl.plot(t,ke,'r')
pl.plot(t,gpe,'g')
pl.plot(t,te,'b')
pl.xlabel('time($s$)')
pl.ylabel('Energy($J$)')
pl.title("Energy Variation of Escaped satellite")
pl.axis([0,0.1e7,-1e9,1e9])
pl.legend(['KE','GPE', 'TE'])
pl.grid()
    
pl.show()
#-----------------------------------Task 4-------------------------------------
def f(z,t):
    xx=z[0] #Displacement in x-direction
    vx=z[1] #Velocity in x-direction
    yy=z[2] #Displacement in y-direction
    vy=z[3] #Velocity in y-direction
  
    ax=-(G*M*xx)/(xx**2+yy**2)**1.5 #Acceleration in x-direction
    ay=-(G*M*yy)/(xx**2+yy**2)**1.5 #Acceleration in y-direction
    d=(xx**2+yy**2)**0.5 #Distance between the centres of mass of the satellite and Mars
 
   
    if d>r:
        return [vx-mv,ax,vy,ay] #Returns required values
        
    else:
        print ("Collision occured at the distance;", d)
        return [0,0,0,0]

'''
to see one particular path
xx0=[10*r, 'velocity in x direction', 10*r,'velocity in y direction ] #The satellite escapes behind Mars
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

t=sp.linspace(0,1e6,2000) #Range of time and interval 

iv=sp.linspace(2.2e4,2.5e4,10) #Range of initial velocity of satellite in x-direction

for v in iv:
    xx5=[-10*r, v, -10*r, 1500] #Initial condition for the satellite that escapes behind Mars
    soln5=spi.odeint(f,xx5,t)
    x=soln5[:,0] #x-displacement
    xv=soln5[:,1] #x-velocity
    y=soln5[:,2] #y-displacement
    yv=soln5[:,3] #y-velocity

    vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
    
    ke=0.5*m*(vs**2) #Kinetic Energy
    gpe=-G*M*m/(x**2+y**2)**0.5 #Gravitational Potential Energy
    te=ke+gpe #Total Energy, to see whether energy conserved

    pl.figure(6)
    pl.plot(t,te,'b')
    pl.legend(['TE'])
    pl.xlabel('time($s$)')
    pl.ylabel('Total Energy($J$)')
    pl.title("Total Energy Variation \n of Satellite escaping behind Mars")
  
    pl.figure(7)
    pl.plot(t,ke,'r')
    pl.legend(['KE'])
    pl.xlabel('time($s$)')
    pl.ylabel('Kinetic Energy ($J$)')
    pl.title("Kinetic Energy Variation \n of Satellite escaping behind Mars")
    
    pl.figure(8)
    pl.plot(t,gpe,'g')
    pl.legend(['GPE'])
    pl.axis([0,1e6,-2.5e9,0.5e9])
    pl.xlabel('Time ($s$)')
    pl.ylabel('Gravitational Potential Energy ($J$)')
    pl.title("Gravitational Potential Energy Variation \n of Satellite escaping behind Mars") 

    pl.figure(9)
    pl.plot(mv*t,t,'o',color='orange') #To trace the motion of Mars
    pl.plot(x,y,'-b') #To trace the motion of the satellite
    pl.axis([-1e8,1e8,-4e7, 4e7]) 
    pl.xlabel('x displacement ($m$)')
    pl.ylabel('y displacement ($m$)')
    pl.legend(['Path of Mars','Path of the satellite'],loc='lower left')
    pl.title('Path of the satellite escaping behind Mars')

pl.show()
#---------------task 4-------------------------------------------------------
def f(k,t):
    xx=k[0] #Displacement in x-direction
    vx=k[1] #Velocity in x-direction
    yy=k[2] #Displacement in y-direction
    vy=k[3] #Velocity in y-direction
  
    ax=-(G*M*xx)/(xx**2+yy**2)**1.5 #Acceleration in x-direction
    ay=-(G*M*yy)/(xx**2+yy**2)**1.5 #Acceleration in y-direction
    d=(xx**2+yy**2)**0.5 #Distance between the centres of mass of the satellite and Mars
 
    if d>r:
        return [vx+mv,ax,vy,ay] #Returns relative x-velocity instead
        
    else:
        print ("Collision occured at the distance;", d)
        return [0,0,0,0]

t=sp.linspace(0,1e6,2000) #Range of time and interval 

iv1=sp.linspace(-2.2e4,-2.5e4,10) #Range of initial velocity of satellite in x-direction

for v1 in iv1:
    xx6=[10*r, v1, 10*r, -1500] #Initial condition for the satellite that escapes behind Mars
    soln6=spi.odeint(f,xx6,t)
    x=soln6[:,0] #x-displacement
    xv=soln6[:,1] #x-velocity
    y=soln6[:,2] #y-displacement
    yv=soln6[:,3] #y-velocity

    vs=(xv**2+yv**2)**0.5 #Magnitude of velocity of the satellite
    
    ke=0.5*m*(vs**2) #Kinetic Energy
    gpe=-G*M*m/(x**2+y**2)**0.5 #Gravitational Potential Energy
    te=ke+gpe #Total Energy, to see whether energy conserved

    pl.figure(10)
    pl.plot(t,te,'b')
    pl.legend(['TE'])
    pl.xlabel('time($s$)')
    pl.ylabel('Total Energy($J$)')
    pl.title("Total Energy Variation \n of Satellite escaping in front of Mars")
  
    pl.figure(11)
    pl.plot(t,ke,'r')
    pl.legend(['KE'])
    pl.xlabel('time($s$)')
    pl.ylabel('Kinetic Energy($J$)')
    pl.title("Kinetic Energy Variation \n of Satellite escaping in front of Mars")
    
    pl.figure(12)
    pl.plot(t,gpe,'g')
    pl.legend(['GPE'])
    pl.axis([0,1e6,-2.5e9,0.5e9])
    pl.xlabel('Time ($s$)')
    pl.ylabel('Gravitational Potential Energy($J$)')
    pl.title("Gravitational Potential Energy \n Variation of Satellite escaping in front of Mars")
    
    pl.figure(13)
    pl.plot(mv*t,t,'o',color='orange') #To trace the motion of Mars
    pl.plot(x,y,'-b')
    
    pl.axis([-1e8,1e8,-4e7, 4e7])
    pl.xlabel('x displacement ($m$)')
    pl.ylabel('y displacement ($m$)')
    pl.legend(['Path of Mars','Path of the satellite'],loc='lower left')
    pl.title('Path of the satellite escaping in front of Mars')

pl.show()
