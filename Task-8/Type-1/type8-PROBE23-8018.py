from itertools import product

alph = sorted('АВОРТ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'ВОРОТА':
        print(pos)
        break