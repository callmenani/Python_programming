from turtle import Turtle as Tut , Screen

timmy = Tut()
timmy.shape("turtle")
for i in range(4):    
    timmy.forward(100)
    timmy.left(90)

Screen().exitonclick()

