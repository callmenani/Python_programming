from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score}",align="center",font=("Arial", 15, "normal"))
        self.hideturtle()
        self.goto(0,270)
    
    def update_score(self):
        self.write(f"Score : {self.score}",align="center",font=("Arial", 15, "normal"))
        
    def game_end(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial", 15, "normal"))
        
    def score_inc(self):
        self.score +=1
        self.clear()
        self.write(f"Score : {self.score}",align="center",font=("Arial", 15, "normal"))
        