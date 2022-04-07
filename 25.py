"""Recursion to Repeat a String n Number of Times
Create a recursive function that takes two parameters and repeats the string n number of times.
The first parameter text is the string to be repeated and the second parameter is the number of times 
the string is to be repeated.
"""

#method 1 

def Recur(a,b):
   i=0
   while i<b:
       print(a)
       i=i+1
str_repeat=input("Enter the string:")
time_repeat=int(input("Enter the number to repeat:"))
Recur(str_repeat,time_repeat)

#method 2

def using_operator(strng,n):
    return strng * n
#by using the star operator

time_repeat=int(input("Enter the number to repeat:"))
print(using_operator("sethu\n",time_repeat))