#Create a left rotation and a right rotation function that returns all the left rotations and right rotations of a string.
#leftRotations("abc") ➞ ["abc", "bca", "cab"]
#rightRotations("abc") ➞ ["abc", "cab", "bca"]
  
str1 = ["abc", "bca", "cab"]


str2 =  ["abc", "cab", "bca"]
def leftrotate(s, d):
   tmp = s[d : ] + s[0 : d]
   return tmp

# In-place rotates s
# towards right by d
def rightrotate(s, d):

   return leftrotate(s, len(s) - d)



print(rightrotate(str2, 2))
print(leftrotate(str1, 2))

# This code is contributed by Rutvik_56