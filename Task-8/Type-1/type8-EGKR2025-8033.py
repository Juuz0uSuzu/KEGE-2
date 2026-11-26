from itertools import *

alph = sorted('ЯНВАРЬ')
ans = []

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] not in 'Я' and 'ЯЯ' not in val and val.count('Ь') <= 1:
        ans.append(pos)
print(max(ans))
