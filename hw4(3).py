# Задание №4
# Определить, какое число в массиве встречается чаще всего.

import random
list_n =[]
for i in range(20):
    list_n.append(random.randint(10, 100))
print(list_n)
n = 0
max_ = 1
for i in range(19):
    a = 1
    for j in range(i+1, 20):
        if list_n[i] == list_n[j]:
            a += 1
    if a > max_:
        max_ = a
        n = list_n[i]
if max_ > 1:
    print(f'Наиболее часто встречаюшиеся число {n}, встречается {max_}')
else:
    print("Встречающихся чисел нет!")
