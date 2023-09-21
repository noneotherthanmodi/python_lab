num=[]
for i in range(3):
    num1 = int(input("Enter values: "))
    num.append(num1)
if num[0]>num[1] and num[2]>num[1]:
    avg = (num[0]+num[2])/2

elif num[1]>num[0] and num[2]>num[0]:
    avg = (num[1]+num[2])/2


elif num[1]>num[2] and num[0]>num[2]:
    avg = (num[1]+num[0])/2

print("Average marks: ",avg)

