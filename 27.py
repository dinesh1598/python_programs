#Define a class/function which has at least two methods: getString:
# to get a string from console input printString: to print the string in upper case. 


class Class:
    
    def __init__(self):
        self.user = input("Enter a String:")
    
    def printString(self):
        upper_case = self.user.upper()
        return upper_case
obj= Class()

print(obj.printString())
