#all odd numbers from 51 and total of 891  
#28123


abundantnumsodd = []
abundantnumseven = []

abundantnumsum = []

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
        abundantnumsodd.append(x)
    elif factorsum > x and x%2==0:
	      abundantnumseven.append(x)
#28123
#all odd numbers from 51 and total of 891
for x in range(0,28124):
    numfactor(x)


#print abundantnumseven

for x in abundantnumseven:
    for y in abundantnumsodd:
        z = x+y
        if z<28124 and z>50:
            abundantnumsum.append(z)
#print abundantnumsum
nums = range(51,28124,2)
remainingnums = set(nums)-set(abundantnumsum)

print "sum is", sum(remainingnums)+891
