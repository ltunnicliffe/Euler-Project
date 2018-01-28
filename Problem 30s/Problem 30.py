import itertools

answers= []
for x in range(7):
	combinations = itertools.product(range(0,11), repeat = x)
	for y in combinations:
			y = list(y)
			#print y
			#print "y is", x
			count = 0
			for q in y:
				#print "q is", q
				count +=q**5
				#print "count is", count
			answer = str(count)
			answerlist = []
			for x in answer:
				answerlist.append(int(x))
			#print "answerlist is", answerlist
			#y = list(y)
			#print "y is", y
			
			if answerlist==y:
				answers.append(count)

	print answers
	print sum(answers)-1


#print permutationlist
