import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_action = input("Enter a choice (rock, paper, scissors): ").lower()
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if(user_action == "rock"):
    image_u = rock
elif(user_action == "paper"):
    image_u = paper
elif(user_action == "scissors"):
    image_u = scissors
if(computer_action == "rock"):
    image_c = rock
elif(computer_action == "paper"):
    image_c = paper
elif(computer_action == "scissors"):
    image_c = scissors
print(f"\nYou chose {user_action} , computer chose {computer_action} .\n")
print(image_u + " " + 'vs' + " " + image_c)

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

