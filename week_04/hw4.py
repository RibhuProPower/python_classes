n = int(input("enter a 2-digit number"))
b = (n%10)
a = int(n/10)
if (n > a**b):
 print(str(n)+" is greater than "+ str(a) + " to the power of " + str(b))
else:
 print(str(n)+" is not greater than "+ str(a) + " to the power of " + str(b))