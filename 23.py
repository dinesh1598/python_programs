#Compare Strings by Count of Characters
#Create a function that takes two strings as arguments and return either True or False depending on 
# whether the total number of characters in the first string is equal to the total number of 
# characters in the second string.

c=input("Enter the string1:")
d=input("Enter the string2:")

#method 1:


def fun(a,b):
   count1=0
   count2=0
   for i in a:
       count1 +=1
   for j in b:
       count2 +=1
   if count1==count2:
       return True
   else:
       return False
  
print(fun(c,d))

#method 2:
def check_len(a,b):
    if len(a)==len(b):
        return True
    else:
        return False
print("by using funtion checking len is equal or not:",check_len(c,d))
    
