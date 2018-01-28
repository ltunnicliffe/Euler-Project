x = 0
y = 1
count = 1
while len(str(y))<1000:
    x = x + y
    count +=1
    
    print count
    #print x
    y = x + y
    count +=1
    #print y
    print count