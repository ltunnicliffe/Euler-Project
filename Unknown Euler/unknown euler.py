s = """3
7 4
2 4 6
8 5 9 3""".split("\n")


mylist = []
for i in s:
    newlist = i.split(" ")
    otherlist=[]
    for x in newlist:
        x = int(x)
        otherlist.append(x)
    mylist.append(otherlist)

print mylist

def routefinder(mylist):
	counts = []
	for x in range(len(mylist)):
		print "x",x
		counter = 0
		for y in range(x+1):
			print "y",y
			value = mylist[x][y]
			counter += value
		counts.append(counter)
	return counts
    

print routefinder(mylist)
