numset = []
for x in range(2,101):
	for y in range(2,101):
		p =x**y
		numset.append(p)
		
realset= set(numset)

print len(realset)