import random
print('''
  ________                                ___________.__               _______               ___.                    ._.
 /  _____/ __ __   ____   ______ ______   \__    ___/|  |__   ____     \      \  __ __  _____\_ |__   ___________    | |
/   \  ___|  |  \_/ __ \ /  ___//  ___/     |    |   |  |  \_/ __ \    /   |   \|  |  \/     \| __ \_/ __ \_  __ \   | |
\    \_\  \  |  /\  ___/ \___ \ \___ \      |    |   |   Y  \  ___/   /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/    \|
 \______  /____/  \___  >____  >____  >     |____|   |___|  /\___  >  \____|__  /____/|__|_|  /___  /\___  >__|       __
        \/            \/     \/     \/                    \/     \/           \/            \/    \/     \/           \/
''')
attempts_remaining = 0
print("Welcome to the Number Guessing Game !")
print("I'm Thinking of Numbers between 1 to 100")
random_guess = random.randint(1,100)
difficulty = input("Which level do you want to play ? Easy or Hard : ").lower()

if difficulty == "easy":
    print("You have 10 attempts to Guess the number")
    for i in range(0,10):
        attempts_remaining =  10 - (i+1)
        user_input = int(input("Enter Your Guess : "))
        if user_input > random_guess :
            print("Too High!")
            print(f"Your remaining attempts are {attempts_remaining}")
            print("Guess again!")
        elif user_input < random_guess:
            print("Too Low!")
            print(f"Your remaining attempts are {attempts_remaining}")
            print("Guess again!")
        else:
            print(f"Yay! Your Guess is correct ! it is {random_guess}.")
        if attempts_remaining == 0:
            print("Sorry you lose!")
            print(f"The Guess number is {random_guess}")
else:
    print("You have 5 attempts to Guess the number")
    for i in range(0,5):
        attempts_remaining =  5 - (i+1)
        user_input = int(input("Enter Your Guess : "))
        if user_input > random_guess :
            print("Too High!")
            print(f"Your remaining attempts are {attempts_remaining}")
            print("Guess again!")
        elif user_input < random_guess:
            print("Too Low!")
            print(f"Your remaining attempts are {attempts_remaining}")
            print("Guess again!")
        else:
            print(f"Yay! Your Guess is correct ! it is {random_guess}.")
        if attempts_remaining == 0:
            print("Sorry you lose!")
            print(f"The Guess number is {random_guess}")