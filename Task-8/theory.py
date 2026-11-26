from itertools import product

# Буквы в алфавитном порядке
alph = sorted('ФОКУС')

# Буквы в обратном алфавитном порядке
alph = sorted('ФОКУС', reverse=True)

# Формирует все возможные комбинации с повторениями
for val in product('ФОКУС', repeat=5):
    val = ''.join(val)
for pos, val in enumerate(product('ФОКУС', repeat=5), start=1):
    val = ''.join(val)
    print(pos, val)
