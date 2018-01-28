import math

def isPrime(n):
    if n == 1:
        return False
    elif n<4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n %3 == 0:
        return False
    else:
        r = math.floor(n**.5)
        f = 5
        while f<=r:
            if n%5 == 0:
                return False
            if n%(f+2)==0:
                return False
            f = f + 6
        return True

    
counter = 0
for x in range(2000000):
    if isPrime(x) == True:
        #print x
        counter +=x
print counter