# euler 1


sum3 = 0
sum5 = 0

for number in range(0,1000):
    
    if number % 3 == 0:
        sum3 += number
    
    elif number % 5 == 0:
        sum5 += number
        
sumtotal = sum3 + sum5
        
print (sumtotal)




# the elif is cool - i think you showed me that on friday