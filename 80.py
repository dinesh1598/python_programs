#Create a function that takes a string and returns it back in camelCase.
#camelCasing("Hello World") ➞ "helloWorld"

def change_str(str):
   temp = str.split('_')
   res = temp[0] + ''.join(ele.title() for ele in temp[1:])
   return res
  
# printing result
str=input("Enter the string:")
print(change_str(str))