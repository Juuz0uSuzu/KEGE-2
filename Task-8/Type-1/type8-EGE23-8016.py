from itertools import *

alph = sorted('АВЛОР')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    if val[0] == 'Л':
        print(pos)
        break