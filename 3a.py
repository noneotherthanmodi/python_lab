sentence = input("Enter a sentence: ")
sp_sen= sentence.split()
print(f"splitted sentence: {sp_sen}")
words = digits = upper = lower = 0

word = len(sp_sen)

for i in sentence:
    if i.isdigit():
        digits += 1
    if i.isupper():
        upper+=1

    if i.islower():
        lower+=1
    
print(f" Number of words: {word} \n Number of digits: {digits} \n Number of lower case: {lower}\n Number of upper case: {upper}")
