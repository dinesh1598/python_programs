#Given a string, reverse all the words which have odd length. The even length words are not changed.


s = input("Enter the sentence:")
words = s.split(' ')
string =[]
for word in words:
   string.insert(0, word)

print("Reversed String:")
print(" ".join(string))
