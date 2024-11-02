from turtle import *
from random import *

penup()
goto(-100,-150) #<-- Set location here
pendown()
left(90)
speed(100)
branch_len=100
angle=30
pencolor('brown')

def branch (branch_len,angle):
    angle=randint(20,40) #<-- Angle randomisation is key here
    sr=uniform(0.55,0.84) #<-- Shrink ratio randomisation is key here
    pensize(branch_len/15)
    if branch_len < 9.1:   #<-- Leaf making functioanlity built in
        pencolor('green')
        stamp()
        pencolor('brown')
        return
    else:
        forward(branch_len)
        left(30)
        branch(sr*branch_len,angle)
        right(60)
        branch(sr*branch_len,angle)
        left(30)
        backward(branch_len)
branch(123,angle)
done()