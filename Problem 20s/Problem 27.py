primes = [2,3,5,7,11,13,17,19]



def primefinder(limit):
    for x in range(limit):
        if x%2==0 or x%3==0 or x%5==0 or x%7==0:
            pass
        else:
            roof = int(x**.5)+1
            for y in range(11, roof):
                if x%y==0:
                    pass
            primes.append(x)





def primer():
    primefinder(2000)
    for x in primes:
        for y in primes:
             stopgap = primerlength(x,y)
             if stopgap>35:
                 print "x is", x, "y is", y, "max prime sequence is", stopgap


def primerlength(a,b):
    counter = 0
    for n in range(800):
        x = (n**2) - a*n + b
        #print x
        counter +=1
        if x<0 or x%2==0 or x%3==0 or x%5==0 or x%7==0:
            return counter-1
        else:
            roof = int(x**.5)+1
            for y in range(11, roof):
                if x%y==0:
                    return counter-1


primer()