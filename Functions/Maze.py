def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
def kadhulu():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
            
       

while at_goal() != True:
    kadhulu()
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
