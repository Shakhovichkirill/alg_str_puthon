# Задание №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.Сами минимальный и максимальный элементы в сумму не включать.

import random

list_n = []
list_m = []
max_ = 0
min_ = 0
s = 0
for i in range(10):
    list_n.append(random.randint(1, 10))
for i in range(10):
    if list_n[i] < list_n[min_]:
        min_ = i
    elif list_n[i] > list_n[max_]:
        max_ = i
if max_ > min_:
    for i in range(min_ + 1, max_):
        s += list_n[i]
else:
    for i in range(max_ + 1, min_):
        s += list_n[i]

print(f'В массиве {list_n}, максимальное число {list_n[max_]}, минимальное число {list_n[min_]}, сумма элементов между этими числами {s}')
