#47. Count occurrence of each elements from list
list = [12,65,3,7,89,64,65,66,3,7,2,3,8,3]

check = int(input("Which element to check: "))
print(list.count(check))


#method 2
from collections import Counter

# declaring the list
l = [12,65,3,7,89,64,65,66,3,7,2,3,8,3]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))
