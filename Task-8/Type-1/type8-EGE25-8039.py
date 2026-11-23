from itertools import product

alph = sorted('ТЕОРИЯ')
ans = []

for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'РТЯ' and val.count('И') >= 2:
        ans.append(pos)

print(max(ans))