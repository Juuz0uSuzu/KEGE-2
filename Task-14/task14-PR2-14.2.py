from string import printable as alph

ans = []
alph = alph[:14]
for x in range(10, 14):
    for y in range(9, x):
        num_1 = int(f'7{alph[x]}37{alph[y]}', 14)
        num_2 = int(f'9{alph[y]}63', x)
        num_3 = int('15148', y)
        num = num_1 + num_2 - num_3
        ans.append([num, num // (x + y)])
print(max(ans))
