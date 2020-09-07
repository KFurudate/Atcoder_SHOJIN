import re

s = input()

s = re.sub(r"\s+", " ", s)
s = s.replace(" ", ",")
print(s)
