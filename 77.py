#Create a function that returns the sum of missing numbers.
#sumMissingNumbers([1, 3, 5, 7, 10]) ➞ 29
#// 2 + 4 + 6 + 8 + 9

lst = [1,2,3,4,5,7,9,11]
def missing_numbers(list1):
    start = lst[0]
    end = lst[-1]
    a = range(start,end+1)
    result = set(a).difference(set(list1))
    return sum(result)
print(missing_numbers(lst))