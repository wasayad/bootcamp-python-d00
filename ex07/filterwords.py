import sys
import string

if len(sys.argv) != 3:
    print("Error wrong number of arguments.")
    exit()

cont = 0
res = list(sys.argv[1])
for check in res:
    if check.isdigit() is True:
        cont = 1
if cont is 1:
    print("Error in arguments.")
    exit()
for check in sys.argv[2]:
    if check.isdigit() is not True:
        cont = 1
if cont is 1:
    print("Error in arguments.")
    exit()
for i in string.punctuation:
    if i in res:
        res.remove(i)
res = ''.join(res)
res = res.split(' ')
res = list(res)
temp = list(res)
for char in temp:
    if len(char) <= int(sys.argv[2]):
        res.remove(char)
print(res)
