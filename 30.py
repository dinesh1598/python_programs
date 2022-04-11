#Write a program that accepts a sentence and 
# calculate the number of letters and digits and also calculates the upper and lower case letters


digit = 0
alphabet = 0
upper = 0
lower = 0
input_string = input("Enter a sentence:")
for i in input_string:
    if i.isalpha():
        alphabet += 1
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        pass
print("Total number of digits is:" + str(digit))
print("Total number of Alphabets in sentence: " + str(alphabet))
print("Total number of Upper in sentence: " + str(upper))
print("Total number of Lower in sentence: " + str(lower))