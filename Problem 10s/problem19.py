months  = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
months2  = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}


count = 0
day = 1


for x in range(1901,2001):
	if x % 4 == 0:
		leap = True
	else:
		leap = False
	for y in range(1,13):
		if leap == False:
			for z in range(1,months[y]+1):
				day +=1
				if day % 7 == 0 and z==1:
					count+=1				
		else:
			for z in range(1,months2[y]+1):
				day +=1
				if day % 7 == 0 and z==1:
					count+=1
				
print count
print day

	
				