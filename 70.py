#Write a program to identify if number is palindrome or not 


#Method 1:
def isPalind(s):

   # Using predefined function to
   # reverse to string print(s)
   rev = ''.join(reversed(s))

   # Checking if both string are
   # equal or not
   if (s == rev):
       return True
   return False


s = input("Enter the string to check:")
ans = isPalind(s)

if (ans):
   print("Yes")
else:
   print("No")


#Method2:

#function which return reverse of a string

def isPalindrome(s):
	return s == s[::-1]



str =input("Enter the string to check:")
ans = isPalindrome(str)

if ans:
	print("the given string is a palindrome:",str)
else:
	print("it is not a palindrome",str)
