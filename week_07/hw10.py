NO1ist=[32,-12,6,-34,89,84,35,98]
biggest=NO1ist[0]

for lpvr in range (1,len(NO1ist)):
    if NO1ist[lpvr]>biggest:
        biggest=NO1ist[lpvr]

print(str(biggest)+' is the biggest number in this list.')