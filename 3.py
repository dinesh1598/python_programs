#Return the Next Number from the Integer Passed

#method 1(normal)

i=int(input("(method1)Enter the number:"))
print("(method1)The next integer is:",i+1)


#method 2(function)
def next_int(value):
    return value+1
    
user_input=int(input("(method 2)Enter the number to print next number:"))    
print(next_int(user_input))