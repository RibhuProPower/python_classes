pal = input('Enter any charecter(s).')
store=pal
pal = pal.replace(' ','')
pal = pal.upper()
ispal=1

for lpvr in range (0,len(pal)):
    if pal[lpvr]!=pal[len(pal)-1-lpvr]:
        ispal=0
        break

if ispal==1:
    print(store+' is a palindrome.')
else:
    print(store+' is not a palindrome.')