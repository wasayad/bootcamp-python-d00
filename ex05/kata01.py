languages =
{'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf', }

temp = ""
temp = list(temp)
string = ' '.join(languages)
string = string.split(' ')
for char in string:
    temp.extend(char)
    temp.extend(" was created by ")
    temp.extend(languages[char])
    temp.extend("\n")
temp = ''.join(temp)
print(temp, end='')
