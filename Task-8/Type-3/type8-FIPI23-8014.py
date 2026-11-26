from string import printable as alph
from itertools import product

ans = 0
for val in product(alph[:6], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 1:
        for i in alph[1:6:2]:
            val = val.replace(i, '*')
        if '*2' not in val and '2*' not in val:
            ans += 1
print(ans)
