ans = []
for N in range(1, 10000):
    R = f'{N:b}'
    R = R + f'{R.count('1') % 2}'
    R = R + f'{sum(int(i) for i in R) % 2}'
    # R = R + f'{sum(map(int, R)) % 2}'
    R = int(R, 2)
    if R > 77:
        ans.append(N)
print(min(ans))
