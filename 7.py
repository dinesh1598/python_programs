#Power Calculator
#method1:
def power(a,b):
   return a**b
 
x=int(input("Enter the number:"))
y=int(input("Enter the number:"))
print(power(x,y))
 
#method2
x=int(input("Enter the base number:"))
y=int(input("Enter the power number:"))
solution=pow(x,y)
print("The answer is:",solution)
 
