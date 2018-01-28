

primeNumbers= []

def primeFinder(y):
	x=2
	while x<y:
		if y%x==0:
			#print "if","y=",y,"x=",x
			break
		elif x==y-1:
			#print "elif prime","y=",y,"x=",x
			primeNumbers.append(y)
			break
		elif x>1000:
			primeNumbers.append(y)
			break
		else:
			#print "else","y=",y,"x=",x
			x=x+1
			

for y in range(2,150000):
	primeFinder(y)

#print primeNumbers

size = len(primeNumbers)

print size

index = 10001

item = primeNumbers[index-2]
print item

		