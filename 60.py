#Check if key exists in dictionary and delete that key value from dictionary

dic ={'a': 1, 'b': 5, 'c': 7}
if 'a' in dic.keys():
    del dic['a']
    print(dic)
