n = int(input("Type any INTEGER."))

isprime = 1
lpvr = 2
while(lpvr < int(n/2) + 1) :
    if (n%lpvr) == 0  :
        print(str(lpvr) + " is a factor of " + str(n))
        isprime = 0
    lpvr += 1
if isprime == 1:
   print(str(n) + " is prime.")