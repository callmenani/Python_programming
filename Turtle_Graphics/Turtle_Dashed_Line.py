from turtle import Turtle as Tut , Screen

timmy = Tut()
timmy.shape("turtle")
for i in range(10):
    timmy.forward(30)
    timmy.penup()
    timmy.forward(30)
    timmy.pendown()
    
    
Screen().exitonclick()