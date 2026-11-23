ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if R.count('1') % 2 == 0:
        R = '11' + R[2:] + '1'
    else:
        if R.count('0') < R.count('1'):
            R += '0'
        else:
            R += '1'
    R = int(R, 2)
    if R > 271:
        ans.append(N)
print(min(ans))
