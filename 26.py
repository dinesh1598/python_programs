#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5. 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#You can take any range like 2000-4700 or 3800-4900 etc 
#Check if both range number also included in output 


#method 1:
lst = []
for i in range(767, 6767):
    if (i % 7 == 0 and i % 5 != 0):
        lst.append(i)
print(lst)


#method 2:

li= []
def check_seven():
    start = int(input("Enter the starting range\n"))
    end = int(input("Enter the ending range\n"))
    for i in range(start, end +1):
        if (i % 7 == 0 and i % 5 != 0):
            li.append(i)
    print(li)
print(check_seven())