print('''
 _____________________
|  _________________  |
| | HN           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

      ''')

import os
def clear(): 
    os.system('cls') 
def add(first_num , second_num):
    return first_num + second_num
def subtract(first_num , second_num):
    return first_num - second_num
def multiply(first_num , second_num):
    return first_num * second_num
def divide(first_num , second_num):
    return first_num / second_num

operations  = {
            "+" : add,
            "-" : subtract,
            "*" : multiply,
            "/" : divide
        }
def Calculator():
    should_continue = True
    num_1 = float(input("Enter the First Number : "))
    while should_continue :
        
        for operators in operations:
            print(operators)

        operation_symbol = input("Choose an Operation from these : ")
        num_2 = float(input("Enter the Second Number : "))
        calculation = operations[operation_symbol]
        answer = calculation(num_1,num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        
        continue_input = input(f"Enter Yes to Calculate again with {answer} or No to fresh Calculation : ").lower()
        if continue_input == "yes":
            num_1 = answer
        else:
            should_continue = True
            clear()
            Calculator()
            
Calculator()