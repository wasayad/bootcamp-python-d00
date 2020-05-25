import sys
argc = len(sys.argv)
i = 0
sep = " "
test = ""
sys.argv.remove(sys.argv[0])
test = sep.join(sys.argv)
test = list(test)
for i in range(0, len(test)):
    if (test[i].isupper() is True):
        test[i] = test[i].lower()
    elif test[i].islower() is True:
        test[i] = test[i].upper()
test.reverse()
test = "".join(test)
print(test)
