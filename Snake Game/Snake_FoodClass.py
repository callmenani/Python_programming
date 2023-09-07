from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        radnom_x = random.randint(-280,280)
        radnom_y = random.randint(-280,280)
        self.refresh()
    def refresh(self):
        
        radnom_x = random.randint(-280,280)
        radnom_y = random.randint(-280,280)
        self.goto(radnom_x,radnom_y)
        