import random
names = input("Enter all of your names who are in the cafe seperated by space : ")
name_list = names.split()
num = len(name_list)
name_index = random.randint(0, num-1)
person_name = name_list[name_index]

print(f"{person_name} have to pay the bill !")