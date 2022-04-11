#. Extend nested list by adding sub list with specific index taken from console

lst = [[2,4,6,8,10],[3,6,9,12,15], [4,8,1,2,16,20], [5,10,15,20,25]]
lst[0].insert(1,1)
print(lst)

lst.append([1,2,3,4,5])
print(lst)

lst[4].append(6)
print(lst)

lst.insert(2,8)
print(lst)

index = int(input("Enter the index at which you have to insert the element:"))
sub_index = int(input("Enter the subindex at which you have to insert the element:"))
element = int(input("Enter the element you want to insert:"))

lst[index].insert(sub_index,element)
print(lst)