import random

def checkprime(n):
    isprime = bool(1)
    for lpvr in range(int(n/2),2,-1):
        if (n%lpvr == 0):
            isprime = bool(0)
            break
    return isprime

randno = random.randint(1,13)
print(checkprime(randno))
print(randno)