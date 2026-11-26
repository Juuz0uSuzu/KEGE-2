from itertools import product

ans = 0
for val in product('ШКОЛА', repeat=3):
    val = ''.join(val)
    if val.count('К')==1:\
        ans+=1
print(ans)