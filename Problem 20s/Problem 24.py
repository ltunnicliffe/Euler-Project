import itertools

def permutation(elements):
    if len(elements) <=1:
        yield elements  # yield is similar to return but gives out elements only once
    else:
        for perm in permutation(elements[1:]):
            for i in range(len(elements)):
							print i
							yield perm[:i] + elements[0:1] + perm[i:]


def permutateme(mylist):
	if len(mylist) <=1:
		return mylist
	else:
		for i in range(len(mylist)):
			print i
			print mylist[:i] + mylist[:i]



list1 = [0,1,2]
list2 = [0,1,2,3,4,5,6,7,8,9]

"""
def factorial(x):
	if x == 0:
		return 1
	else:
		return factorial(x-1)*x
		
x = factorial(10)

print 1000000.00/x
"""
#x = itertools.permutations(list2)
#x.sort()
x = permutation(list1)

lists=[]
for y in x:
	#lists.append(y)
	print y

#lists.sort()
#print lists[999999]



