#Write a program to perform all basic mathematical operations 
num1 = input('Enter first number: ') 
num2 = input('Enter second number: ') 

sum = float(num1) + float(num2) 

min = float(num1) - float(num2) 
mul = float(num1) * float(num2) 
div = float(num1) / float(num2) 

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum)) 

print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min)) 
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul)) 
# 
print('The division of {0} and {1} is {2}'.format(num1, num2, div))