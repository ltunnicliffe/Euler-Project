import itertools #30 = 
possiblecombs = []
for x in range(50):
	list = itertools.combinations_with_replacement((x for x in [1,2,5,10,20,50]), x)
	for y in list:
		if sum(y) == 100:
			possiblecombs.append(y)
	

#print possiblecombs
print len(possiblecombs)+1+1