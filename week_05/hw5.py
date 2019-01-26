n = int(input("Enter any POSITIVE INTEGER."))
lpvr = 1
fact = 1
while (lpvr <= n):
    fact = fact * lpvr
    lpvr += 1
print (str(n) + " factorial is " + str(fact))