MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 350,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 450,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
def resource_check(sufficient):
    for items in sufficient:
        if sufficient[items] >= resources[items]:
            print(f"Sorry {items} is'nt enough!")
            return False
    return True

def transaction_check(money_recieved , cost_of_item):
    if money_recieved >= cost_of_item:
        change = round(money_recieved - cost_of_item , 2)
        print(f"Here is Your Change {change}")
        return True 
    else:
        print("Sorry Your Money is'nt sufficient, it is Refunded")
        return False
def make_coffee(drink_name , order_resources):
    for item in order_resources:
        resources[item] -= order_resources[item]
    print(f"Here is your drink name {drink_name}")
    
is_on =  True
while is_on:
    user_input = input("What do you want to order (Espresso/Latte/Cappuccino) : ").lower()
    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        print(f'''
    Water : {resources["water"]}
    Milk : {resources["water"]}
    Coffee : {resources["coffee"]}
            ''')
    else:
        drink = MENU[user_input]
        if resource_check(drink['ingredients']):
            user_topup = int(input("Topup your account by adding money : "))
            if transaction_check(user_topup , drink['cost']):
                money = user_topup
                make_coffee(user_input , drink['ingredients'])
            
    
        