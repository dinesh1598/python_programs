"""Remove items from list 
list1 = [54, 44, 27, 79, 91, 41]
Out
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""

li=[54, 44, 27, 79, 91, 41]
print("it removes the last items in the list:",li.pop())
print("it is another method in pop:",li.pop(0))

del li[-4]
print("After removing the index of -4:",li)
li.insert(2,2)
print("List after Adding element at index 2 :",li)
li.append(12)
print("List after Adding element at last :",li)
print("it remove all elements from the list:",li.clear())