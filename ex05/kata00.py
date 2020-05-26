import sys
import re

t = (19, 42, 21)

if len(t) is 0:
    print("Tupple error please enter valid tupple.")
    exit()

test = "The "
test = list(test)
test.extend(str(len(t)))
test.extend(" numbers are: ")
temp = "".join(str(t))
temp = temp.replace('(', '')
temp = temp.replace(')', '')
for i in range(0, len(temp)):
    if temp[i].isdigit() != 1 and temp[i] != ',' and temp[i] != ' ':
        print("Tupple error only numbers are authorised.")
        exit()
test.extend(temp)
test = ''.join(test)
print(test)
