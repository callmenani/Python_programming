from turtle import Turtle as Tut , Screen
import random
timmy = Tut()
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw(sides):
    angle = 360/sides
    for i in range(sides):
        timmy.forward(100)
        timmy.right(angle)
    
for x in range(3,11):
    draw(x)
    timmy.color(random.choice(colours))
Screen().exitonclick()