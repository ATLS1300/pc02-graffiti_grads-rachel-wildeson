#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Rachel Wildeson
September 6 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
import turtle 
turtle.speed(10)

#Left Eye
turtle.up()
turtle.goto(-15, 100)
turtle.down()
turtle.begin_fill()
turtle.color(128,0,0)
turtle.circle(15)
turtle.end_fill()

turtle.up()
turtle.goto(-15,110)
turtle.down()
turtle.pensize(2)
turtle.color(255,255,255)
turtle.circle(3)

#Right Eye
turtle.up()
turtle.goto(38,110)
turtle.down()
turtle.begin_fill()
turtle.color(128,0,0)
turtle.circle(15)
turtle.end_fill()

turtle.up()
turtle.goto(42,120)
turtle.down()
turtle.pensize(2)
turtle.color(255,255,255)
turtle.circle(3)

#Eyebrows
turtle.up()
turtle.goto(-45, 160)
turtle.down()
turtle.pensize(6)
turtle.color(0,0,0)
turtle.setheading(-25)
turtle.forward(55)

turtle.setheading(30)
turtle.forward(55)

#Finger Handle
turtle.up()
turtle.goto(80,-70)
turtle.down()
turtle.pensize(10)
for i in range(4): 
     turtle.color(255,255,0)
     turtle.right(90)
     turtle.forward(40)
 
 #Sword
turtle.up()
turtle.goto(88,-80) 
turtle.down()
turtle.pensize(30)
turtle.color(192, 192, 192)
turtle.forward(165)   
 
#Mouth
turtle.up()
turtle.goto(-15,40)
turtle.down()
turtle.pensize(3)
turtle.begin_fill()
turtle.color(128,0,0)
turtle.setheading(50)
for i in range(3):
        turtle.color(128,0,0)
        turtle.forward(30)
        turtle.right(50)
turtle.end_fill()


#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
