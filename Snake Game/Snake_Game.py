from turtle import Turtle,Screen
import time
from Snake_MoveClass import Snake
from Snake_FoodClass import Food
from Snake_Scoreboard import Scoreboard
tom = Turtle()
scr = Screen()

scr.setup(600,600)
scr.bgcolor("black")
scr.title("Nag Raj")
scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_on = True

while game_on:
    scr.update()
    time.sleep(0.2)
    
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.score_inc()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        game_on = False
        score.game_end()
        
    for segment in snake.new_seg:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_end()




scr.exitonclick()