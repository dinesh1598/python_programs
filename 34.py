#write a program to sort the data by ascending and descending order
#Take list of data - you can take input from console or define list

lst = [29,74,73,56,22,98]
def sort_li(lit):
    lit.sort()
    return lit
print(sort_li(lst))
def sort_li_reverse(lit):
    lit.reverse()
    return lit
print(sort_li_reverse(lst))

#method 2

number=[1,5,6,9,0]
def ascen(number):
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i]>number[j]:
                number[i],number[j]=number[j],number[i]
    print("The ascending order is:",
          number)
def descending(number):
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i]<number[j]:
                number[i],number[j]=number[j],number[i]
    print("The decending order is:",number)
    
ascen(number)
descending(number)

