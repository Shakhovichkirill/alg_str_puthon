# Задание 4
# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
a1 = int(input("Введите нижнюю границу целого числа: "))
b1 = int(input("Введите верхнбб границу целого числа: "))
r1 = random.randint(a1, b1)
print(r1)

a2 = float(input("Введите нижнюю границу вещественного числа: "))
b2 = float(input("Введите верхнбб границу вещественного числа: "))
r2 = random.uniform(a2, b2)
print(r2)

a3 = ord(input("Введите нижнюю границу символов: "))
b3 = ord(input("Введите верхнюю границу символов: "))
r3 = random.randint(a3, b3)
print(chr(r3))
