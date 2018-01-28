#78498
def isPrimeMach6(limit):  # for the 6n+-1 test - under 1,000,000 in 3.7 seconds and 2,000,000 primes in 9.7 seconds
	primes = [2,3,5,7,11,13,17]	
	for x in range(18,limit):
		test = True
		if x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0 or x%17==0:
				test = False
		else:
				roof = int((x**.5+1)/6)+1  #ceiling necessary for checking whether number has factors
				for trialnum in range(3,roof):
					if x%(6*trialnum-1) == 0 or x%(6*trialnum+1) == 0:
						test = False
						break
				if test == True:
					primes.append(x)
	return primes

"""
def isPrimeFermatClass(n):
	if x%2 == 0:
		return False
	if (((7**(n-1))-1)%n) == 0:
		return True
"""
primes = isPrimeMach6(1000000)
#print primes
print len(primes)
	