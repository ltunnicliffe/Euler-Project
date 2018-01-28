decimaldic = {}
stringbit = "1"
newstring = "00000000"
for x in range(250):
    stringbit = stringbit + newstring
    
intstring = int(stringbit)
#print stringbit


for x in range(1,1000):
    answer =  str(intstring/x)
    if len(answer)>9:
        if answer[4]!=answer[5] or answer[5] != answer [6] or answer[7] != answer[8]:
            if answer.find(answer[0:50],1)!=-1 and answer.count(answer[0:50])<3:
                counter = answer.count(answer[0:50])
                print "x is", x, "and counter is", counter
                decimaldic[x] = answer

 
            
    
print decimaldic