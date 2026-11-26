ans = []
for N in range(3, 41):
    R = f'{N:b}'
    if R[-4:] == '1011':
        ans.append([N, R])
print(max(ans)[0])