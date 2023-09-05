from turtle import Turtle,Screen
import random

race_on = False
scr = Screen()
scr.setup(width=500,height=400)
bet = scr.textinput(title="Place Your Bet!" , prompt="Which Turtle will win the race : ")
colors = ['red', 'yellow' , 'blue' , 'green' , 'purple' , 'orange']
y_positions = [-70 , -40 , -10 , 20 ,50 ,80 ]
new_tom = []
for tr in range(0,6):
    tom = Turtle(shape="turtle")
    tom.color(colors[tr])
    tom.penup()
    tom.goto(x=-230,y=y_positions[tr])
    new_tom.append(tom)
    
if bet:
    race_on = True
    
while race_on:
    for toms in new_tom :
        if toms.xcor() > 230:
            race_on = False
            winning_color = toms.pencolor()
            if winning_color == bet:
                print("You won!")
            else:
                print(f"You Lost ! {winning_color} have won")
                
        toms.forward(random.randint(0,10))
                
                
    


scr.exitonclick()