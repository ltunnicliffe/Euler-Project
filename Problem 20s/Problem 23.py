abundantnums = []

def numfactor(x):
    factors =[]
    roof = int(x**.5)+1
    for n in range(1,roof):
        if x%n==0:
            factors.append(n)
            otherfactor = x/n
            if n!=otherfactor and otherfactor!=x:
                factors.append(otherfactor)
    factorsum = sum(factors)
    if factorsum > x and x%2!=0:
        abundantnums.append(x)
#28123
#all odd numbers from 51 and total of 891
for x in range(0,50):
    numfactor(x)

abundantnumsum = []

for x in abundantnums:
    for y in abundantnums:
        z = x+y
        if z<100:
            abundantnumsum.append(z)

print set(abundantnumsum)

nums = range(50)

answer = set(nums)- set(abundantnumsum)
realanswer = sum(answer)

print realanswer



