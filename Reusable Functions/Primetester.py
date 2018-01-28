primes = [2,3]

def primecounter():
    counter = 1
    for x in primes:
        counter = counter*x
    counter = counter+1
    primetester(counter)


def primetester(counter):
    roof = (int(counter**.5)+1)
    for x in range(2,roof):
        if counter%x==0:
            primetester(x)
    if counter not in primes:
        primes.append(counter)
    if len(primes)>10:
        return "Test Complete"
    print primes
    primecounter()




primecounter()