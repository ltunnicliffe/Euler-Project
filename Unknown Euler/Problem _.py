import itertools

answers= []
permutationlist =[]
y= [8,2,0,8]
	#print "y is", x
count = 0
for q in y:
	#print "q is", q
	count +=q**4
#print "count is", count
answer = str(count)
answerlist = []
for x in answer:
	answerlist.append(int(x))
	#print "answerlist is", answerlist
y = list(y)
	#print "y is", y
	
if answerlist==y:
	answers.append(count)
	

print answers
print sum(answers)
#print permutationlist

