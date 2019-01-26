
s = int(input("Type the smaller INTEGER."))
b = int(input("Type the bigger INTEGER."))


for n in range(s,b):
    isprime = 1
    lpvr = 2
    while(lpvr < int(n/2) + 1) :
        if (n%lpvr) == 0  :
            isprime = 0
            break
        lpvr += 1
    if isprime == 1:
        print(str(n) + " is prime.")