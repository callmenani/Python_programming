from turtle import Turtle as Tut , Screen
import turtle
import random
timmy = Tut()
turtle.colormode(255)
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0,90,180,270]
def rand_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colours_2 = (r , g, b)
    return colours_2 
    
    

timmy.pensize(10)
timmy.speed("fastest")
for i in range(100):
    timmy.color(rand_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


Screen().exitonclick()