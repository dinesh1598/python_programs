#.Concant two list index wise 
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

#original lists
print ("original list 1 : " + str(list1))
print ("original list 2 : " + str(list2))
# concatenation
res = [i + j for i, j in zip(list1, list2)]
# printing result
print ("The list after element concatenation is : " + str(res))
