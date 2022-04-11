#Slice list into 3 chunks and reverse each chunks 
#sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89] 


my_list = [11,53,54, 45, 8, 23, 14, 12, 78, 45, 89]
def slice_chunks(l, n):
   for i in range(0, len(l), n):
       yield l[i:i + n]
          
n = int(input("Enter the number to cut the list in piece:"))
x = list(slice_chunks(my_list, n))
print (x)