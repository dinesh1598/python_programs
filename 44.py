#Create a list by picking an odd-index items from the first list and even index items from the second
#l1 = [3, 6, 9, 12, 15, 18, 21]
#l2 = [4, 8, 12, 16, 20, 24, 28] 
#Output 
#Element at odd-index positions from list one
#[6, 12, 18]
#Element at even-index positions from list two
#[4, 12, 20, 28]
#Printing Final third list
#[6, 12, 18, 4, 12, 20, 28]


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
new_l1=l1[1::2]
print("odd index items from l1:",new_l1)
new_l2=l2[::2]
print("Even index items from l2:",new_l2)
final=new_l1+new_l2
print("finally:",final)
