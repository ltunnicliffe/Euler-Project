#Prime Number Test Function-  



def isPrimeMach6(x):  # for the 6n+-1 test - under 1,000,000 in 6.24 seconds and 2,000,000 primes in 15.5 seconds
	if x<2 or x%2==0 and x!=2 or x%3==0 and x!=3:
		return False
	else:
		roof = int(x**.5)+1  #ceiling necessary for checking whether number has factors
		for trialnum in range(1,(roof/6+1)):
					if x%(6*trialnum-1) == 0 or x%(6*trialnum+1) == 0:
						return False
		return True

def isPrimeMach2(x): #for 2 step with roof, 6.36 seconds for primes to a million 78498 and for two million is 16.3 seconds
	if x<2 or x%2==0 and x!=2 or x%3==0 and x!=3:
			return False
	else:
		roof = int(x**.5)+1  #ceiling necessary for checking whether number has factors
		for trialnum in range(3,roof,2):
				if x%trialnum == 0:
					return False
		return True

def isPrimeFermatClass(x): #uses Fermat's little theorem to estimate primes
	if (7**x)%7==7:
		return False
	else:
		return True
	

def sieveAlpha1(limit): #simple prime sieve, speed for p per 1000000 is off the scale!
	a = range(2,limit)
	for x in a:
		n=x
		print "n is ", n, "x is", x
		while x*n <= limit-1:
			if x*n in a:
				a.remove(x*n)
			n+=1
	print len(a)

#sieveAlpha1(100)



#sieveBeta(100)
def sieveDelta(limit): #suprisingly slow!
	a=list(range(2,limit))
	for x in a:
	    comp=[]
	    for y in range(a.index(x),len(a)):
	        q=x*a[y]
	        if q<=max(a):
	            comp.append(q)
	        else:
	            break
	    for z in comp:
	        a.remove(z)
	print len(a)

#sieveDelta(100)
#call Prime Number Test Function and stores primes in list

primes = []	
for x in range(2,100):
	if isPrimeFermatClass(x) == True:
		primes.append(x)
		
answer = len(primes)
print answer