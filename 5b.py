import re

phone = re.compile(r'\+\d{12}')
email = re.compile(r'\S+@+\S+\.+[A-Za-z]{2,}')

with open('example.txt','r') as f:
    for line in f:
        matches = phone.findall(line)
        for match in matches:
            print(match)


        matches = email.findall(line)
        for match in matches:
            print(match)

    