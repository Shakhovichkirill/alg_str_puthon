# Задание №9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = []
M = 5
N = 4

for i in range(N):
     b = []
     print(f'Строка {i}')
     for j in range(M):
         a = int(input(f'Введите значение {j}: '))
         b.append(a)
     matrix.append(b)

for line in matrix:
    for i, item in enumerate(line):
        print(f'{item:>5}', end='')
    print()

max_ = -1
for j in range(M):
    min_ = 10
    for i in range(N):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]
    if min_ > max_:
        max_ = min_
print('-' * (len(matrix[0]) * 6))
print("Максимальный среди минимальных: ", max_)
