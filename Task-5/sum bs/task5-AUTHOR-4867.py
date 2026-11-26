ans = []
for N in range(2, 10_000):
    sum_1 = sum(map(lambda x: int(x) if int(x) % 2 == 0 else 0, str(N)))
    sum_2 = sum(map(int, str(N)[1::2]))
    R = abs(sum_1 - sum_2)
    if R == 9:
        ans.append(N)
print(ans[0])