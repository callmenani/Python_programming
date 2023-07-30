height = float(input("What is Your height : "))
weight = float(input("What is Your weight : "))
bmi = round(weight/height**2)
if(bmi < 18.5):
    print(f"Your bmi is {bmi} , You are under weight !")
elif(bmi < 25):
    print(f"Your bmi is {bmi} , You are normal weight !")
elif(bmi < 30):
    print(f"Your bmi is {bmi} , You are over weight !")
elif(bmi < 35):
    print(f"Your bmi is {bmi} , You are obese !")
else:
    print(f"Your bmi is {bmi} , You are clinically obese !")