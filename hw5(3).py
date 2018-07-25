# Задание №5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
n = 5
list_n =[]
for i in range(1,n+1):
    list_n.append(random.randint(-100, 100))
print(list_n)
i = 0
j = 0
while i < n:
    if list_n[i] < 0 and j == 0:
        j = i
    elif list_n[i] < 0 and list_n[i] > list_n[j]:
        j = i
    i += 1
print(f'Максимальный отрицательный элемент: {list_n[j]} на позиции {j}')