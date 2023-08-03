

def prime_checker(number) :
    prime = True
    for i in range(2,number):
        if number%i==0:
            prime = False

    if prime:
        print(f"{number} is a Prime")
    else:
        print(f"{number} is Not a Prime")

n = int(input("Check this number: "))
prime_checker(number=n)
