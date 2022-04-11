#Write a program to square each odd number in a list. 
#Take a list - list contains at least 20 elements
li=[12,14,16,14,122,76,23,978,32,76,35,45,19,26,27,20,16,27]
#method 1

for i in li:
    if i%2!=0:
        print(i**2)
        
#method 2:(using list compersion)


result = [i**2 for i in li if i%2 != 0]
print(result)