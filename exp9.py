str1=str(input("Enter string 1"))
str2=str(input("Enter string 2"))
if len(str1) == len(str2):
    print("strings with same length")
    for i in range(len(str1)):
        print(str1[i],end=" ")
        print(str2[i],end=" ")
else:
    print("strings with different length")
