#!/usr/bin/env python



num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for a in range(1,num+1):
    for a in range(1,num+1-a):
        print("*",end="")
    print()   





def reverse(string): 
    string = string[::-1] 
    return string 
  
s = "ineuron"
  
print (s) 
  
print (reverse(s))



