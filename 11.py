"""
    The Farm Problem
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

"""
#method 1
class Animals:
    def __init__(leg_count,chick,cow,pig):
        leg_count.chickens=chick
        leg_count.cows=cow
        leg_count.pigs=pig
    def calculate_leg(leg_count):
        ch=leg_count.chickens*2
        C=leg_count.cows*4
        P=leg_count.pigs*4
        total_legs=ch+C+P
        return total_legs
    
ob=Animals(7,3,4)
print(ob.calculate_leg())

#method2(normal method)
cows=int(input("Enter the count of cows:"))
pig=int(input("Enter the count of pig:"))
chick=int(input("Entr the count of check:"))
total_legs=(cows*4)+(pig*4)+(chick*2)
print("The total legs:",total_legs)

        