import math, turtle

screen=turtle.Screen()
screen.setup(width=800, height=600, startx=200, starty=-200)
screen.bgcolor('black')
pen=turtle.Turtle()
pen.speed(40)
n=20
d=31
# n=62
# d=59
pen.color('white')
pen.pensize(1.5)

for theta in range(361):
    k=theta*d*math.pi/180
    r=300*math.sin(n*k)
    x=r*math.cos(k)
    y=r*math.sin(k)
    pen.goto(x,y)

turtle.done()

