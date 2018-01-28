#2081 way with fives, ones and twos only  2081
#when there is a hundred, 17950 ways
#1 way when there is a 200
#when there are two fifties = 9631 ways 
#when there are four fifties = 1 way
#when there is one fifty  =  14382  ways
#when there are three fifties = 1380  ways
#when there tens = 15192

print 2081 + 17950 + 1 + 9631 + 1 + 14382 + 1380 + 15192


starter = 100
for x in range(200/starter):
	remainder = 200 - 100
	list = [1,2,5,10]