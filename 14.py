"""
Check if objOne Is Equal to objTwo
Create a function that checks to see if two object arguments are equal to one another. 
Return True if the objects are equal, otherwise, return False.
"""

#method 1

def object(a, b):
   
   if a ==b :
       return True
   else:
       return False
list1 = [24, 34, 56, 65]
list2 = [24, 34, 56, 65]

print(object(list1, list2))

#method 2
list1 = [24, 3, 6,17, 65]
list2 = [9, 18,12, 65]
if list1==list2:
    print(True)
else:
    print(False)