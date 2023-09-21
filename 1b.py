num = int(input("Enter a number: "))
given = str(num)

if given == given[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

for i in range(10):
    if given.count(str(i)):
        print(str(i),"appears: ",given.count(str(i)),"times")
        
