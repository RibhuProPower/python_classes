tiny = int(input("Enter the tinier number."))
HUGE = int(input("Enter the huger number."))
ListA = []
for invr in range (tiny,HUGE + 1):
    n = 1
    while (invr > 10 ** n):
        n = n + 1

    timesrun = 0
    add = 0
    while timesrun < n:
        add += (((invr % (10 ** (timesrun + 1))) - (invr % (10 ** (timesrun)))) /(10 ** timesrun)) ** n
        timesrun += 1
    if add == invr:
        ListA.append(invr)
    else:
        pass
if len (ListA) == 0:
    print("There are no armstrong numbers between " + str(tiny)  + " and " + str(HUGE) + ".")
else:
    print("The armstrong numbers between " + str(tiny) + " and " + str(HUGE) + " are " + str(ListA) + ".")