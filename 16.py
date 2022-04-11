#Find the Smallest Number in a List
#Create a function that takes a list of numbers and returns the smallest number in the list.
lis=[23,6,34,9,58,2,18]
#method 1   

def diff(l):
   l.sort()
   print("the list after sort (method 1):",l)
   
   small=l[0]
   return small
  
print(diff(lis))

#method 2(using min())
def diff(li):
    return min(li)
print("The smallest value in the list using min() (method 2):",diff(lis))


#method 3


def smallest(list):
    min=list[0]
    for a in list:
        if a <min:
            min=a
    return min
    

print("The smallest value in the list(method 3):",smallest(lis))

