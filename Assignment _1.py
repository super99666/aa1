#!/usr/bin/env python
# coding: utf-8




n = []
for i in range(2000,2701):
    if (i%7==0)and (i%5==0):
        n.append(str(i))
print(','.join(n)) 




s = "sudheer pillala".split()
n =" "
for i in s[::]:
    n = n+" "+i
    



n      
       


import math

r = 12

volume = 3/4 * math.pi* math.pow(r,3)

print("volume of sphere is:{0:2f}".format(volume))





