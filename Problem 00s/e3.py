# third euler problem
# to find the prime factors for any given number

# this was my original code. i'll modify it when i get the chance. 
# having thought about the square root rule for largest prime factors,
# it does make sense..!


text = input('what number do you want to check prime factors for? ')
number = int(text)
newnumber = int(number**.5)
for counter in range(1,newnumber):
	if number%counter == 0:
		print "checker new", counter
		primecounter = int(counter**.5)+1
		print "primecounter",primecounter
		for x in range(1,primecounter):
			if primecounter%x == 0:
				break
		print "newcounter", counter
				