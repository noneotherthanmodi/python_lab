import re

num = (input("Enter number in the specific format: "))

def isphonenumber(number):
    if len(number) != 12:
        return False
    if number[3]!='-' or number[7]!='-':
        return False
    for i in range(12):
        if i==3 or i==7:
            continue
        if not number[i].isdigit():
            return False
        
    return True

def isnumber(number):
    expression = r'\d{3}-\d{3}-\d{4}'
    match = re.fullmatch(expression,number)

    return match is not None

choice = int(input("1. Without 2. with : "))
if choice==1:
    res = isphonenumber(num)
    if res==True:
        print("Matched")
    else:
        print("Not matched")

elif choice==2:
    res = isnumber(num)
    if res==True:
        print("Matched")
    else:
        print("Not matched")
else:
    exit(0)




