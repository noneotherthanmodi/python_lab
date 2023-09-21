str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1)<len(str2):
    short = len(str1)
    long = len(str2)

else:
    short = len(str2)
    long = len(str1)


count = 0
for i in range(short):
    if str1[i]==str2[i]:
        count+=1


print(count/long)


