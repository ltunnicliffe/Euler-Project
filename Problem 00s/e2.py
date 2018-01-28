# second euler problem

# the fibonacci sequence:

a = 0
b = 1

sumeven = 0

for number in range(100):
    (a,b) = (b, a+b)  


# even numbers in the fibonacci sequence:
    if b < 4000000:
    
        if b % 2 == 0:
            sumeven += b

print (sumeven)




# the range(100) is arbitrary and so, i think, not the best way to do it.
# I wanted sth along the lines of, if b is not less than 4000000, stop counting,
# but I don't know how to stop the for..in..: from counting.