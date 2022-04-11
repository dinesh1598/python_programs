#Divides Evenly
#Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.

a=int(input("Enter the number:"))
b=int(input("Enter the number 2:"))
def check_even(c,d):
    if (c%d == 0):
        return True
    else:
        return False
print(check_even(a,b))