from itertools import product

alph = sorted('АКЛМНЯ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] == 'К' and val[1] == 'М':
        print(pos)
        break