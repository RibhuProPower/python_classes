n = int(input("enter a 2-digit number"))
d = int(input("enter a single-digit number"))
if (n%10) == d :
    print("The number contains "+ str(d)+ " in the units digit")
if int(n/10) == d:
    print("The number contains "+ str(d)+ " in the tens digit")
if (n%10 != d) and (int(n/10) !=d ):
    print("The number does not contain " + str(d) + " in either digit")