
s = int(input("Type the smaller INTEGER."))
b = int(input("Type the bigger INTEGER."))


for n in range(s,b):
    isprime = 1
    for lpvr in range(int(n/2),2,-1):
        if (n%lpvr == 0):
            isprime = 0
    if isprime == 1:
        print(str(n) + " is prime.")