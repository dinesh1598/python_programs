#Convert list into dictionary and add new item into dictionary

fruits = ["appple", "orange", "banana", "kiwi"]
prices = [1,2,6,8]

fruit_dictionary = dict(zip(fruits, prices))
fruit_dictionary.update({'lichi':3})

print(fruit_dictionary)