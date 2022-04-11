#Take two list and Iterate both list simultaneously and print outputimport itertools
list1 = [56, 78, 12, 45, 34, 29]
list2 = [29, 34, 45, 12, 78, 56]

for (a,b) in zip(list1,list2):
   print(a,b)


