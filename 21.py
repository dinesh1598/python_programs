#Check if an Integer is Divisible By Five
#Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.

#method 1:
num=int(input("Enter the number to check:"))
def fun(value):
   if value%5==0:
       return True
   else:
       return False
print("The sum is:",fun(num))

