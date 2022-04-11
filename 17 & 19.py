#Difference of Max and Min Numbers in List
#Create a function that takes a list and returns the difference between the biggest
#and smallest numbers
lis=[23,6,34,9,58,2,18]
#method 1

def diff(l):
   l.sort()
   print("the list after sort:",l)
   large=l[-1]
   small=l[0]
   difference=large-small
   return difference
print(diff(lis))

#method2:(using min() and max())

def diff(l):
    large=max(l)
    small=min(l)
    difference=large-small
    return difference
print("The difference between two number using min() and max() is:",diff(lis))

#method3:


def fun(a):
   big_num = a[0]
   for num in a:
       if num > big_num:
           big_num = num
   small_num = a[0]   
   for num in a:
       if num < small_num:
           small_num = num
   different = big_num-small_num
   return different

print("The difference is:",fun(lis))