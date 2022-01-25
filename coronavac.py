from turtle import *
import turtle

speed(100)
color('cyan')
bgcolor('black')
b = 200
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

turtle.forward(100)
turtle.getscreen()
turtle.getcanvas().postscript(file="corona.eps")
