from itertools import *

alph = sorted('ПОБЕДА')
ans = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if (val[0] == 'О' and val.count('П') == 1 and val.count('О') == 1
            and val.count('Б') == 1 and val.count('Е') == 1
            and val.count('Д') == 1 and val.count('А') == 1):
        if pos % 2 == 0:
            ans.append(pos)
print(max(ans))