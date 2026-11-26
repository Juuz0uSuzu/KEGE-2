from string import printable as alph
from itertools import product

ans = 0
for val in product(alph[:7], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        for i in alph[0:7:2]:
            val = val.replace(i, '*')
        for i in alph[1:7:2]:
            val = val.replace(i, '#')
        if '**' not in val and '##' not in val:
            ans += 1
print(ans)
