import re

f = open('email.txt')
content = f.read()
f.close()
matches = re.findall('((\w+)@\w+\.\w+)', content)
print(matches)
