import sys
import re

phrase = "The right format"

test = ""
test = list(test)
for i in range(0, 41 - len(phrase)):
    test.extend("-")
test.extend(phrase)
test = ''.join(test)
print(test)
