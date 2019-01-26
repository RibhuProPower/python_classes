n = int(input("Type any INTEGER."))

isprime = 1
for lpvr in range(2,int(n/2)) :
    if (n%lpvr) == 0 :
        isprime = 0
        break
#if isprime == 0 :
    #print(str(n) +  " is composite.")
#else :
    #print(str(n) + " is prime.")

isprime = 1
lpvr = 2
while(lpvr < int(n/2) + 1) :
    if (n%lpvr) == 0  :
        isprime = 0
        break
    lpvr += 1
if isprime == 0:
    print(str(n) + " is composite.")
else:
    print(str(n) + " is prime.")