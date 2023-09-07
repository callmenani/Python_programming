from turtle import Turtle

SEGS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.new_seg = []
        self.create_snake()
        self.head = self.new_seg[0]
        
    def create_snake(self):
        for position in SEGS:
            self.add_segment(position)
            
    def add_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.new_seg.append(seg)
    
    def extend(self):
        self.add_segment(self.new_seg[-1].position())
    
    def move(self):
        for sq in range(len(self.new_seg) - 1,0,-1):
            new_x = self.new_seg[sq-1].xcor()
            new_y = self.new_seg[sq-1].ycor()
            self.new_seg[sq].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    
