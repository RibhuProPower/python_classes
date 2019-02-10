terms = int(input('Please enter a POSITIVE INTEGER.'))
ListA = [0,1]
Kulchaasimsim = 0
while Kulchaasimsim<=terms-3:
    ListA.append(ListA[Kulchaasimsim]+ListA[Kulchaasimsim+1])
    Kulchaasimsim+=1
print(ListA)