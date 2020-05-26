import sys
import re

date = (3, 30, 2019, 9, 25)

data = str(date)
data = data.replace('(', '')
data = data.replace(')', '')
data = data.split(', ')
string = ""
string = list(string)
if int(data[0]) > 24 or int(data[0]) < 0:
    print("Error hours argument can't exceed 24 or goes under 0.")
    exit()
elif int(data[1]) > 60 or int(data[1]) < 0:
    print("Error minutes argument can't exceed 60 or goes under 0.")
    exit()
elif int(data[3]) < 0 or int(data[3]) > 12:
    print("Error mounth argument can't exceed 12 or goes under 0.")
    exit()
elif int(data[4]) < 0 or int(data[4]) > 31:
    print("Error days argument can't exceed 31 or goes under 0.")
    exit()
string.extend(data[3])
string.extend("/")
string.extend(data[4])
string.extend("/")
string.extend(data[2])
string.extend(" ")
string.extend(data[0])
string.extend(":")
string.extend(data[1])
string = ''.join(string)
print(string)
