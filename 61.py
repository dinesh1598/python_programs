#Get only unique items from dictionary


my_dict = {'name':'dinesh', 'age':23, 'address':'vellore', 'name':'sethu',
'short_name':'sethu'}
print(set(my_dict))

#method my_dict = {'name':'dinesh', 'age':23, 'address':'vellore', 'name':'sethu','short_name':'sethu'}

print(set(my_dict.values()))

#Using dictionary comprehensions
res = list(set(val for dic in my_dict for val in my_dict.values()))
print(str(res))