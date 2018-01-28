def collatznumcounter(n):
    counter = 0
    while n !=1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        counter +=1
        #print n
    return counter+1



def bigcollatz():
    bigcounter = 0
    bigcollatz = 1
    for x in range(1,1000000):
        counter = collatznumcounter(x)
        if counter>bigcounter:
            bigcounter = counter
            bigcollatz = x
    print "the number with the longest sequence is", bigcollatz, "and the length of the sequence is", bigcounter



bigcollatz()