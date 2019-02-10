n=77
sum = 0

for lpvr in range (1,n+1):
    sum+=lpvr

print('The sum is '+str(sum)+'.')

#with while
sum=0
lpvr=1
while lpvr <= n:
    sum+=lpvr
    lpvr+=1
print('The sum is '+str(sum)+'.')