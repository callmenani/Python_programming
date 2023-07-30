print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("Which direction you want to go ? left or right : ").lower()
if(direction == "left"):
    swin_wait = input("You are now at a huge lake do want to wait for the boat or swim ? : ").lower()
    if(swin_wait == "wait"):
        house_colour = input("There are three houses infront of you 'Red , Green , Blue' what do you want to choose : ").lower()
        if(house_colour == "green"):
            print("Yay! you've found the treasure enjoy :)")
        elif(house_colour == "red"):
            print("You are trapped in a maze , Game over !")
        elif(house_colour == "blue"):
            print("The house is full of wild dogs :( Game Over ! ")
        else:
            print("Sorry you've entered into a wrong house! the was locked you can't go outside Game Over :(")
    else:
        print("You are eaten by a huge crocodile! Game Over")      
else:
    print("Sorry you've choosen a wrong direction you fell into a valley :( Game Over ")