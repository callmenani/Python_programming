print("Welcome to Universal Kingdom ! ")
height = int(input("Please enter your height : "))
age = int(input("Please enter your age : "))

if(height >= 120):
    print("Yayy! you cann ride the RollarCoaster :)")
    if(age < 12):
        print("You have to pay 500/- for entry")
    elif(age <= 18):
        print("You have to pay 300/- for entry")
    else:
        print("You have to pay 700/- for entry")
else:
    print("Sorry you are not eligible for RollarCoaster :(")
