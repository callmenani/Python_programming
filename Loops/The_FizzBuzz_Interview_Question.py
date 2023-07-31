for i in range(0,101):
    if(i%3==0 and i%5==0):
        i = "FizzBuzz"
    elif(i%3==0):
        i = "Fizz"
    elif(i%5==0):
        i = "Buzz"
    print(i)
    