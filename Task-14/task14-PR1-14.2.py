from string import printable as alph

for x in alph[:20]:
    num_1 = int(f'627{x}J8', 20)
    num_2 = int(f'H45I{x}5HIJ', 20)
    num_3 = int(f'4IDB49J{x}7', 20)
    num = num_1 + num_2 + num_3
    if num % 19 == 0:
        print(num//19)
