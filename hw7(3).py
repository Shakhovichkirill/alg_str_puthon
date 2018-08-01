# Задание №7
# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

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
for i in list_n:
    list_m.append(i)
list_m.remove(list_n[min_])
min_1 = 0
i = 0
for i in range(9):
    if list_m[i] < list_m[min_1]:
        min_1 = i
print(f'Два минимальных числа {list_n[min_]} и {list_m[min_1]}')