import turtle
import os

os.chdir(os.path.dirname(__file__))

tr = turtle.Turtle()
wn = turtle.Screen()
wn = turtle.addshape('superMarioSprite.gif')
tr.shape('superMarioSprite.gif')

turtle.done()