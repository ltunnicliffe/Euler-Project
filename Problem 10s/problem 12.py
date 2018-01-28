

triangles = []
def triangularnum(limit):
	for n in range(limit):
		n = (n*(n+1))/2
		if n%3==0 and n%2 == 0 and n%5 ==0 and n%7 ==0:
			triangles.append(n)

	
triangularnum(100000)

for x in triangles:
	counter = 0
	roof = int(x**.5)
	for y in range(2,roof):
		if x%y==0:
			counter +=1
	if counter>250:
		print counter, "the number is ", x
		break

