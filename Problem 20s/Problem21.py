def findfactor(x):
	factors = []
	roof = int(x**.5)+1
	for y in range(1,roof):
		#print y
		if x%y == 0:
			if y>1:
				otherfactor = x/y
				if y != otherfactor:
					factors.append(otherfactor)
			factors.append(y)
	factorsum = sum(factors)
	return factorsum
			
sums = {}
for x in range(10000):
	factorsum = findfactor(x)
	sums[x]=factorsum

	
#print sums
counter = 0
for x in sums:
	for y in sums:
		if sums[x]==y and sums[y] == x and y !=x:
			print x, y
			counter +=x
print counter
	