from itertools import product

ans = 0
for val in product('ВИШНЯ', repeat=6):
    val = ''.join(val)
    if val[0] != 'Ш' and val[-1] not in 'ИЯ' and val.count('В') <= 1:
        ans += 1
print(ans)