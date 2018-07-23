# Задание №8
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = []
M = 5
N = 4

for i in range(N):
    b = []
    print(f'Строка {i}')
    for j in range(M - 1):
        a = int(input("Введите значение: "))
        b.append(a)
    matrix.append(b)

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>5}', end='')
    print(f'  | {sum_line}')
