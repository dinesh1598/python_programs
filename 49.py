#Concatenate two list in following 
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]  output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']



#method1
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result=[]

for i in list1:
  for j in list2:
      result.append(i+j)
print(result)



#method 2
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

for i in test_list2 :
    test_list1.append(i)

print ("Concatenated lists: " + str(test_list1))