#X**2+y**2=25

#while x<y<5:
#y=0


def isWhole(x):
	if(x%1 == 0):
		return True
	else:
		return False


for y in range(100,500):
	for x in range(100,500):
		z=((x**2)+(y**2))**(.5)
		if isWhole(y)==True:
			if x+y+z==1000:
				print "x is", x, "y is", y, "z is", z
				answer = x*y*z
				print answer
				
			






