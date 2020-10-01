from turtle import *
from math import pi,sin,cos

penup()
setpos(0,0)
pendown()

hideturtle()
speed(1)
pensize(10)
a=200
for l in range(0,100):
    t = l/10
    
    x = a*cos(t)*(1-cos(t))
    y = a*sin(t)*(1-cos(t))
    setpos(x,y)
penup()
setpos(0,0)