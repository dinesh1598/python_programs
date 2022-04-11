#Get the Sum of All List Elements
#Create a function that takes a list and returns the sum of all numbers in the list.
li=[0.14,67,23,12,36]
#method 1

def lst_sum(listt):
    sum = 0
    for i in listt:
        sum += i
    return sum
print(lst_sum(li))

#method 2

#Approach Three: Using while loop
def sum_li(l):
    count = 0
    a = 0
    while (a < len(l)):
        count = count + l[a]
        a =a+1
    return count


print(sum_li(li))