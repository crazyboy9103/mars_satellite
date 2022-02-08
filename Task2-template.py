#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 02:14:05 2016

@author: davidgill
"""
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
 

  return [vx,ax,vy,ay] #Return the values


t=sp.linspace(0.,1000000.,1000)


xx0=[7*r, -1000, 3*r, 1000] #Initial conditions as required

soln=spi.odeint(f,xx0,t) 

print (soln)

x=soln[:,0] #x-displacement
vx=soln[:,1] #x-velocity
y=soln[:,2] #y-displacement
vy=soln[:,3] #y-velocity

pl.figure(1,)
pl.title("Path of the satellite")
pl.axis([-4e7, 4e7, -5e7, 3e7])
pl.plot(x,y)
pl.xlabel("x-displacement ($m$)")
pl.ylabel("y-displacement ($m$)")

pl.show()
