import os
def clear(): 
    os.system('cls') 

print("Welcome to the Kane's Auction")
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')




my_auction = {}
bidding_finished = False

while not bidding_finished:
    def adding(name, bid):
        my_auction[name] = int(bid)

    name_input = input("Enter Your Name: ")
    bid_input = input("What's Your Bid: ")

    adding(name_input, bid_input)

    continue_check = input("Do you want to enter details again? Yes or No: ").lower()
    if continue_check == 'no':
        bidding_finished = True

# Find the highest bid and name of the person
highest_bid = 0
winner_name = ""

for name, bid in my_auction.items():
    if bid > highest_bid:
        highest_bid = bid
        winner_name = name
        print(f"The highest bid is {highest_bid} by {winner_name}.")
    elif continue_check == 'yes':
         clear()
