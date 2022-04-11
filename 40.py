#write a program to print the duplicates number from the list.
# Print output in comma separated list 


li=[12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,12,88,7,6,2]
new = []
for a in li:
   n = li.count(a)
   if n > 1:      

       if new.count(a) == 0:

           new.append(a)

print("duplicate value:",new)

