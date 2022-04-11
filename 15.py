#Find the Largest Number in a List
#Create a function that takes a list of numbers. Return the largest number in the list.

#method 1:(using funtion)
from re import L


li=[9,2,15,623,75,23,18,33]
li2=["apple","banana","cherry","doll","easy","Fish","g","hour","ice","jack","knee"]


def largest(list):
    max=list[0]
    for a in list:
        if a >max:
            max=a
    return max
    

print("The largest value in the list:",largest(li))


#method 2:using sort with funtion
def easy_method(value):
    value.sort()
    return value[-1]

print("By using sort method to find largest value:",easy_method(li))


#method 3

def easy(e):
  return len(e)


li2.sort(key=easy)

print("by using the length of the string:",li2)


