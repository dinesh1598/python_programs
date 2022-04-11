#Define a function that can accept two strings as input and print the string with maximum length 
# in the console. If two strings have the same length, then the function 
# should print all strings line by line.

 
def strings(str1,str2):
   if len(str1)>len(str2):
       print(str1)
   elif len(str1)<len(str2):
       print(str2)
   elif len(str1)==len(str2):
       print(str1,str2,sep="\n" )
   else:
       print("invalid string:")
  
strings(input("Enter a string: "), input("Enter another string: "))
