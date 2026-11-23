from string import printable as alph

for x in alph[:22]:
    num_1 = int(f'27{x}98966', 22)
    num_2 = int(f'26{x}33', 22)
    num_3 = int(f'522{x}5', 22)
    num = num_1 + num_2 + num_3
    if num % 21 == 0:
        print(num // 21)
