vowels="aeiouAEIOU"
word=input("Enter a word: ")
flag=20
for char in word:
    if char in vowels:
        flag=1
        break
    if(flag==1):
        print("Given string contains vowel")
else:
    print("Given string not contains vowel")


