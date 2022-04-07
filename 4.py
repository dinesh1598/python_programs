#4.Return the Remainder from Two Numbers
#method 1(Normal)

a=int(input("Enter the number(1):"))
b=int(input("Enter the number(2):"))
c=a%b
print("The remainder is:",c)

#method 2(using function)

def remain(c,d):
    return c%d
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print("The remainder is:",remain(a,b))