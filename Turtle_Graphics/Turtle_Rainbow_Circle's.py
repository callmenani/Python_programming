from turtle import Turtle as Tut , Screen
import turtle
import random
timmy = Tut()
turtle.colormode(255)
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def rand_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colours_2 = (r , g, b)
    return colours_2 

timmy.speed("fastest")

def new_head(n):
    for i in range(int(360/n)):
        timmy.color(rand_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + n)
    

new_head(5)



Screen().exitonclick()