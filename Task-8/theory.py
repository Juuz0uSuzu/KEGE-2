from itertools import product
from timeit import repeat

# Формирует все возможные комбинации с повторениями
for val in product('ФОКУС', repeat=5):
    val = ''.join(val)
for pos, val in enumerate(product('ФОКУС', repeat=5), start=1):
    val = ''.join(val)
    print(pos, val)
