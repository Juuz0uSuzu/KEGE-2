ans = []
for x in range(10, 67):
    for y in range(0, x):
        num_1 = 7*67**4 + 3*67**3 + x*67**2 + 1*67**1 + y*67**0
        num_2 = 4*x**3 + 9*x**2 + y*x**1 + 6*x**0
        num = num_1 + num_2
        if num not in ans:
            ans.append(num)
print(len(ans))