from string import printable as alph

for x in alph[:22]:
    num_1 = int(f'12313{x}57', 22)
    num_2 = int(f'1{x}34561', 22)
    num = num_1 + num_2
    if num % 21 == 0:
        print(num // 21)