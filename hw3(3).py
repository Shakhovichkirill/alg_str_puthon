# Задание №3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

list_n = []
list_m = []
for i in range(10):
    list_n.append(random.randint(10, 100))
print(list_n)
max_ = 0
min_ = 0
for i in range(10):
    if list_n[i] < list_n[min_]:
        min_ = i
    elif list_n[i] > list_n[max_]:
        max_ = i
list_n[max_], list_n[min_] = list_n[min_], list_n[max_]
for i in list_n:
    list_m.append(i)
print(list_m)
