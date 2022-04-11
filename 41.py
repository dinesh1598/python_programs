
#write a program which accepts a string from the console and print it in reverse order.

#method 1

def rev(value):
   rev_str=""
   for i in value:
       rev_str=i+rev_str
      
   return rev_str
get_in=input("Enter the string to reverse:")
print(rev(get_in))

#method 2


def reverse(string):
   string = string[::-1]
   return string

s = "mindbowser"
print(reverse(s))

#method 3

def reverse(string):
   string = "".join(reversed(string))
   return string
s = "mindbowser"
print (s)
print (reverse(s))