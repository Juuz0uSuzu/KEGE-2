from itertools import product

alph = sorted('АЛГОРИТМ')
ans = []

for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'АГ' and val.count('Р') >= 2:
        ans.append(pos)

print(min(ans))