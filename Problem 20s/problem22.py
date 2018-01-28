f = open('/Users/luketunnicliffe/Desktop/names.txt')
for x in f:
	lines = x.split(",")

f.close()

names = []
for x in lines:
	y = x.replace('"','')
	names.append(y)

names.sort()

#print names

length = len(names)
counters = []
coutner = 0
section =1
for x in names:
	
	counter = 0
	for y in x:
		
		counter+= ord(y)-64
	counter = counter * section
	section+=1
	counters.append(counter)
	
print sum(counters)