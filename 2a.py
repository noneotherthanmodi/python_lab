def func(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return func(n-1)+func(n-2)

num = int(input("Enter a number:"))
if num>0:
    print(f"func({num})","=",func(num))
else:
    print("incorrect input")

