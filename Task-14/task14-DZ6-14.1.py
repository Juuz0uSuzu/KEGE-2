def sum_7(n):
    s = 0
    while n > 0:
        s += n % 7
        n //= 7
    return s

for x in range(1, 1000):
    num = 3 * 7**(x + 1) + 13 * 7**(x + 2) + 31 * 7**(3 * x) + 1 * 7**(2 * x)
    if sum_7(num) == 18:
        print(f"{x}")
        break