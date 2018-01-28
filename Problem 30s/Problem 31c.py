import itertools


list = [1,2,5,10]
variable = 200
count = 0
for y in range(1,101):
	results = itertools.combinations_with_replacement(list,y)
    	for x in results:
			if sum(x) == variable:
				count +=1
				#print x
print "variable is", variable, "count is", count



#10 is 11
#50 is 342
#variables for 5 plus 10/5 - 10/1 = 6, plus 1 10
#variables for 50: 10 for 5 = 10*4, 50 for 2  = 25 -50, plus 1 50, 5 for 10*11


#2081 way with fives, ones and twos only  2081
#when there is a hundred, 17950 ways
#1 way when there is a 200
#when there are two fifties = 9631 ways 
#when there are four fifties = 1 way
#when there is one fifty  =  14382  ways
#when there are three fifties = 1380  ways
#when there tens = 15192