#Return new set of identical items from two sets

answer = []
set1 = {15,12,8,5,3,1}
set2 = {12,13,5,77,11}
for i in set1:
    for j in set2:
        if i == j:
            answer.append(j)
            
print(set(answer))