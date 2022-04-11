"""
Write a program to check the validity of password input by users. 
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 7
No space accepted
Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1, Then, the output of the program should be: ABd1234@1

"""


special_characters = ["!","@",'#','$','%','^','&','*','(',')']
alphabet = 0
digit = 0
whitespace = 0
upper = 0
sc = 0
user_input = input("Enter your password")
for i in user_input:
    if i.isalpha():
        alphabet += 1
    if i.isupper():
        upper += 1
    elif i.isdigit():
        digit += 1
    elif i in special_characters:
        sc += 1
    else:
        whitespace += 1
if (len(input_string)>= 7 and alphabet > 0 and digit>0 and upper > 0 and whitespace
==0 and sc > 0):print("Password Accepted")
else:
    print("Password Denied")