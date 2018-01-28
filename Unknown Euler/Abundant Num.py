for x in range(0,28123,2):
    abundantdouble = numfactor(x)
    



abundantnumsum = []

for x in abundantnums:
    for y in abundantnums:
        z = x+y
        if z<28123:
            abundantnumsum.append(z)
            
for q in abundantnumsum:
    if q in nums:
        nums.remove(q)
print "sum is", sum(nums)


        
        
       
print len(abundantnums)
print "nums length is", len(nums) 




mylist = [12*x for x in range(1000)]
mylist2 = [18*x for x in range(1000)]
mylist3 = [20*x for x in range(1000)]
mylist4 = [30*x for x in range(1000)]
mylist5 = []
newlist = (((set(abundantnums) - set(mylist)) - set(mylist2)) - set(mylist3))
newlist = newlist-set(mylist4)

print newlist

