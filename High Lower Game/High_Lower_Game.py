from game_data_HL import data
import random
import os
def clear(): 
    os.system('cls') 
logo = '''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/    
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
      '''
def game():
    print(logo)
    score = 0
    game_should_continue = True
    first_choice = random.choice(data)
    second_choice = random.choice(data)
    while game_should_continue:
        first_choice = second_choice
        second_choice = random.choice(data)
        while first_choice == second_choice:
            second_choice = random.choice(data)
        check_1 = int(first_choice['follower_count'])
        check_2 = int(second_choice['follower_count'])

        print(f"Compare A : {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
        print('''
                 _    __    
                | |  / /____
                | | / / ___/
                | |/ (__  ) 
                |___/____(_)
            ''')
        print(f"Compare B : {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

        user_answer = input("Who has more followers? Type 'A' or 'B':").lower()
        
        clear()
        print(logo)

        if user_answer == 'a':
            if check_1 > check_2 :
                score += 1
                print(f"Your right!, Your Score is {score}")
            else:
                game_should_continue = False
                print(f"Your Guess is Wrong, Your Score is {score}")
                
        elif user_answer == 'b':
            if check_2 > check_1:
                score += 1
                print(f"Your right!, Your Score is {score}")
            else:
                game_should_continue = False
                print(f"Your Guess is Wrong, Your Score is {score}")
game()            
 