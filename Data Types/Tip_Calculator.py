print("Welcome to the Tip Calculator !")
total_bill = float(input("What is the total bill : $"))
tip = int(input("What percentage of tip you to give ? 10,12 or 15 : "))
people = int(input("How many people to split the bill : "))
bill_with_tip = tip/100 * total_bill + total_bill
bill_per_person = bill_with_tip/people
final_bill = round(bill_per_person , 2)
print(f"Each person sould pay :  ${final_bill}")
 
