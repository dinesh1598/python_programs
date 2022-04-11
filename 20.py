"""_Return the Last Element in a List
Create a function that accepts a list and returns the last item in the list. 
The list can be either homogeneous or heterogeneous

"""

#method1:(hetrogeneous)
li=[12,"aravindh",1,9,4,"raghul",66,73,49]
def Last_item(l):
   return l[-1]
print("The last item in the list",Last_item(li))


#method1: homogenous1
li=[12,1,9,4,66,73,4]
def Last_item(l):
   return l[-1]
print("The last item in the list",Last_item(li))



#method 2:homogeneous2:
li=["dinesh","raghuk","sethu","mohan","vineeth"]
def Last_item(l):
   return l[-1]
print("The last item in the list",Last_item(li))