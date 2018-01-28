y = 3
p = 5
q = 9
t = 7

y = 1
p = 1
q = 1
t = 1


a = 8
b = 4
c = 2
d = 6


answer = 1
for x in range(0,500):

    subanswer = 0
    y += x*8+c
    p += x*8+b
    q += x*8+a
    t += x*8+d
    print y, p, q, t

    subanswer = y + p + q + t
    answer+=subanswer
    print answer