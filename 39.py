#write a program to print the list after removing the 0th,4th,5th numbers from list 
#List [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,01].
li = [12, 24, 35, 70, 88, 120, 155, 99, 12, 7, 8, 93, 67, 47, 76, 34, 43, 76, 23, 1]
new_list = []

for index, value in enumerate(li):
  if index not in (0, 4, 5):
      new_list.append(value)

print(new_list)