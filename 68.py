#Create a function that takes a list and string. The function should remove the
#letters in the string from the list, 
# and return the list.
li = ['a','b','c','d','e','f','g','h','i','j']
input_string = input("Enter a string\n")
def cut_out_char(lst, str):
    for i in str:
        if i in lst:
            lst.remove(i)
        return lst
print(cut_out_char(li,input_string))