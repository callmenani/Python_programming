from turtle import Turtle,Screen

tom = Turtle()
scr = Screen()

tom.shape("turtle")

def move_front():
    tom.forward(10)
def move_back():
    tom.backward(10)
def turn_right():
    tom.right(90)
def turn_left():
    tom.left(90)
    
def clear():
    tom.clear()
    tom.penup()
    tom.pendown
    tom.home()
scr.listen()
scr.onkey(key='d' , fun=move_front)
scr.onkey(key='a' , fun=move_back)
scr.onkey(key='w' , fun=turn_left)
scr.onkey(key='s' , fun=turn_right)
scr.onkey(key='c' , fun=clear)



scr.exitonclick()