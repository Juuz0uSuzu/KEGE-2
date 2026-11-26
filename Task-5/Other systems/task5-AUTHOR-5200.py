ans = []
for N in range(1, 10000):
    R = f'{N:o}'
    if (R.count('0') + R.count('2') + R.count('4') + R.count('6')) % 2 != 0:
        R = R[-3:] + '46'
    else:
        R = f'{(N % 8) * 5:o}' + R

    R = int(R, 8)

    if R == N:
        ans.append(N)
print(min(ans))