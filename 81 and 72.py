#Check if given char is vowel or consonant 

vowel=['a','e','i','o','u','A','E','i','o','u']
def check(letter,alphabets_letter):
   if alphabets_letter not in letter:
       print("the given letter is a consonanat:",alphabets_letter)
   else:
       print("The given letter is a vowel:",alphabets_letter)
       
  
  
  
  
  
alphabets=input("Enter the only alphabets to check:")
check(vowel,alphabets)