student_heights = input("Enter student heights : ").split()
num = 0 
sum = 0
for x in student_heights:
    y = int(x)
    sum += y 
    num += 1

avg = sum/num

print(round(avg))