import re
f = open('input.txt').read()

t1 = t2 = 0
rgx = r"(mul\(\d+\,\d+\))|(do\(\))|(don\'t\(\))"
enabled = True
for match in re.finditer(rgx, f):
    if match.group(1):
        d1, d2 = match.group(1).split(',')
        d1, d2 = int(d1[4:]), int(d2[:-1])
        mltp = d1 * d2
        t1 += mltp
        t2 += mltp * enabled
    else:
        enabled = bool(match.group(2))
   
print(t1)
print(t2)