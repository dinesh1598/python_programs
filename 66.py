#Create a function that takes a number and returns its length(use of the len()
#function is prohibited)


def string_length():
    count = 0
    str = input("Enter a string:")
    for i in str:
        count += 1
    return count
print(string_length())