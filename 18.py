#Concatenating Two Integer Lists
#Create a function to concatenate two integer lists.


li1=[81,82,85,38,122]
li2=[15,12,6,3,8,25,94]

#method 1(using (+) operator)
concatenate=li1+li2
print("Concatenate using + operator:",concatenate)



#method 2
def con(a,b):
    c=a+b
    return c
    
    
print("The concatenation list is:",con(li1,li2))

#method 3
def con(a,b):
    a.extend(b)
    return a
    
    
print("The concatenation list is:",con(li1,li2))


