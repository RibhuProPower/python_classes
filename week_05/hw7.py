invr = int(input("Enter a POSITIVE INTEGER."))

n = 1
while (invr > 10 ** n):
    n = n + 1

timesrun = 0
add = 0
while timesrun < n:
    add += (((invr % (10 ** (timesrun + 1))) - (invr % (10 ** (timesrun)))) /(10 ** timesrun)) ** n
    timesrun += 1
if add == invr:
    print ("This number is Armstrong")
else:
    print("This number isn't Armstrong")