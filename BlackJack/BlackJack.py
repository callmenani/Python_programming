import random
import os
def clear(): 
    os.system('cls') 
def blackjack():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    
    while True:
        user_score = 0
        comp_score = 0
        usercard_1 = random.choice(cards)
        usercard_2 = random.choice(cards)
        user_score = usercard_1 + usercard_2
        compcard_1 = random.choice(cards)
        compcard_2 = random.choice(cards)
        comp_score = compcard_1 + compcard_2

        print(f"Your draws are {usercard_1} and {usercard_2}")
        print(f"Computer first card is {compcard_1}")

        def user_win():
            print("You Won!")
            print(f"Your Score is {user_score} and computer score is {comp_score}")
        def comp_win():
            print("Computer Won!")
            print(f"Your Score is {user_score} and computer score is {comp_score}")
        def draw():
            print("Your Scores are draw!")
            print(f"Your Score is {user_score} and computer score is {comp_score}")

        take_new = input("Do you want to draw another card? 'Yes' or 'No': ").lower()

        if take_new == 'yes':
            usercard_3 = random.choice(cards)
            if usercard_3 == 11 and user_score > 10:
                usercard_3 = 1
            user_score += usercard_3
            print(f"Your new pick is {usercard_3}")

            if user_score > 21:
                if comp_score < 21:
                    print("Computer Won!")
                else:
                    print("You Lost!")
            elif comp_score > 21:
                if user_score < 21:
                    print("You Won!")
                else:
                    print("Computer Lost!")
            elif user_score == 21:
                user_win()
            elif comp_score > 21 or (user_score < 21 and user_score > comp_score):
                user_win()
            elif comp_score == 21 or user_score < comp_score:
                comp_win()
            elif user_score == comp_score:
                draw()
        else:
            if user_score == 21:
                user_win()
            elif comp_score > 21 or (user_score < 21 and user_score > comp_score):
                user_win()
            elif comp_score == 21 or user_score < comp_score:
                comp_win()
            elif user_score == comp_score:
                draw()
        
        play_again = input("Play again? enter Yes/No : ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
        else:
            clear()

blackjack()
