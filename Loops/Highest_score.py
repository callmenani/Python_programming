student_scores = input("Input a list of student scores : ").split()
highest = 0

for x in student_scores:

    y = int(x)
    if(y > highest):
        highest = y
print(student_scores)
print(f"The Highest Score among the Students is  : {highest}")