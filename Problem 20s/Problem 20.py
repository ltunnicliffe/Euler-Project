def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

    
def stringer(x):
    count = 0
    mystring = str(factorial(x))
    for x in mystring:
        num = int(x)
        count += num
    return count
        

print stringer(100)