print("Welcome to Luffy's Kitchen ! ")
pizza_size = input("Please enter your pizza size 'S,M,L' : ")
pepperoni = input("Do you want to add pepperoni in your pizza 'Y or N' : ")
extra_cheese = input("Do you want to add extra cheese in your pizza 'Y or N' : ")
bill = 0

if(pizza_size == 'S'):
    bill += 200
elif(pizza_size == 'M'):
    bill += 300
else:
    bill += 500

if(pepperoni == 'Y'):
    if(pizza_size == "S"):
        bill += 15
    else:
        bill += 30
if(extra_cheese == 'Y'):
    bill += 20
    
print(f"You total bill is {bill} !")



