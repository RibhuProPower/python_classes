RibhuTup=(1,9999999999,9876,bool(1),'qwertyuiop',123456789.1,32452.2345,bool(0),'asdfghjkl','zxcvbnm',3546,bool(1),456.5467)

currentstart = 0
currentslicenumber=0
newList=[]
for lpvr in range (0,len(RibhuTup)-1):
    if type(RibhuTup[lpvr]) != type(RibhuTup[lpvr+1]):
        #print(RibhuTup[currentstart:lpvr+1])
        newList.append(RibhuTup[currentstart:lpvr+1])
        currentstart = lpvr+1
        currentslicenumber+=1
#print(RibhuTup[0:3])

#print(newList)

for list in newList:
    print(list)