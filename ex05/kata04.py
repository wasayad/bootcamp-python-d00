import sys
import re

t = (0, 4, 132.42222, 10000, 12345.67)

string = str(t)
string = string.replace('(', '')
string = string.replace(')', '')
string = string.split(', ')

ret = ""
ret = list(ret)
if int(string[0]) < 0 or int(string[0]) > 99:
    print("Error in tupple.")
    exit()
if int(string[1]) < 0 or int(string[1]) > 99:
    print("Error in tupple.")
    exit()
if int(string[0]) > 9:
    ret.extend("day_")
else:
    ret.extend("day_0")
ret.extend(string[0])
ret.extend(", ")
if int(string[1]) > 9:
    ret.extend("ex_")
else:
    ret.extend("ex_0")
ret.extend(string[1])
ret.extend(" : ")
string = list(string)
string.remove(string[0])
string.remove(string[0])
temp = string[0]
i = 0
while temp[i] != '.' and temp[i]:
    ret.extend(temp[i])
    i = i + 1
j = 0
while j < 3 and temp[i + j]:
    ret.extend(temp[i + j])
    j = j + 1
ret.extend(", ")
string.remove(string[0])
for i in range(0, len(string)):
    temp = string[i]
    j = 0
    for d in range(0, len(temp)):
        if (temp[d] == '.'):
            break
        j = j + 1
    ret.extend(temp[0])
    ret.extend(".")
    ret.extend(temp[1])
    ret.extend(temp[2])
    if (j < 10):
        ret.extend("e+0")
    else:
        ret.extend("e+")
    ret.extend(str(j - 1))
    if i < len(string) - 1:
        ret.extend(", ")
ret = ''.join(ret)
print(ret)
