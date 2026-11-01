ans = []
for N in range(1, 10_000):
    R = f'{N:b}'
    if R[-1] == '0':
        R = R + '10'
    else:
        R = '1' + R + '01'

    R = int(R, 2)
    if R > 516:
        ans.append(N)

print(min(ans))