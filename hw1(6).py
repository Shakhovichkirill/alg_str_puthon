# Задание №1
#  Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.

# Версия Python - 3.7
# Разрядность ОС - x64

# №1
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.Сами минимальный и максимальный элементы в сумму не включать.
import random
from alg_str_puthon.memory_def import total_size, show_size

list_n = []
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

d = dict(a=s, b=list_n)

#####################################################################
print(total_size(d, verbose=True))
print(total_size(list_n, verbose=True))
print(total_size(s, verbose=True))

"""
list_n
472 - полный объем памяти списка и его объектов
192 <class 'list'> [3, 5, 8, 10, 6, 8, 2, 3, 4, 7] - 192 байта размер списка
28 <class 'int'> 3    - 28 байт память затрачиваемая на каждый объект списка
28 <class 'int'> 5    
28 <class 'int'> 8    
28 <class 'int'> 10
28 <class 'int'> 6
28 <class 'int'> 8
28 <class 'int'> 2
28 <class 'int'> 3
28 <class 'int'> 4
28 <class 'int'> 7
28 <class 'int'> 14

s
28 <class 'int'> 18 - память затрачиваемая на переменную s - не относится к списку выше
28 - соответственно ее полный объем

d
840 - полный объем памяти словаря и его элементов
240 <class 'dict'> {'a': 19, 'b': [6, 4, 10, 7, 4, 8, 1, 4, 9, 6]}
50 <class 'str'> 'a'
28 <class 'int'> 19
50 <class 'str'> 'b'
192 <class 'list'> [6, 4, 10, 7, 4, 8, 1, 4, 9, 6]
28 <class 'int'> 6
28 <class 'int'> 4
28 <class 'int'> 10
28 <class 'int'> 7
28 <class 'int'> 4
28 <class 'int'> 8
28 <class 'int'> 1
28 <class 'int'> 4
28 <class 'int'> 9
28 <class 'int'> 6
"""
######################################################################
print(show_size(list_n))
print(show_size(s))
print(show_size(d))
"""
list_n
type = <class 'list'>, size = 192, object = [4, 1, 8, 3, 7, 9, 8, 3, 1, 7] - - 192 байта размер списка

	 type = <class 'int'>, size = 28, object = 4 - 28 байт- память затрачиваемая на каждый объект списка
	 type = <class 'int'>, size = 28, object = 1
	 type = <class 'int'>, size = 28, object = 8
	 type = <class 'int'>, size = 28, object = 3
	 type = <class 'int'>, size = 28, object = 7
	 type = <class 'int'>, size = 28, object = 9
	 type = <class 'int'>, size = 28, object = 8
	 type = <class 'int'>, size = 28, object = 3
	 type = <class 'int'>, size = 28, object = 1
	 type = <class 'int'>, size = 28, object = 7
	 
s
 type = <class 'int'>, size = 28, object = 18
 
 d 
 type = <class 'dict'>, size = 240, object = {'a': 10, 'b': [10, 10, 1, 4, 6, 3, 5, 1, 7, 4]}
	 type = <class 'tuple'>, size = 64, object = ('a', 10)
		 type = <class 'str'>, size = 50, object = a
		 type = <class 'int'>, size = 28, object = 10
	 type = <class 'tuple'>, size = 64, object = ('b', [10, 10, 1, 4, 6, 3, 5, 1, 7, 4])
		 type = <class 'str'>, size = 50, object = b
		 type = <class 'list'>, size = 192, object = [10, 10, 1, 4, 6, 3, 5, 1, 7, 4]
			 type = <class 'int'>, size = 28, object = 10
			 type = <class 'int'>, size = 28, object = 10
			 type = <class 'int'>, size = 28, object = 1
			 type = <class 'int'>, size = 28, object = 4
			 type = <class 'int'>, size = 28, object = 6
			 type = <class 'int'>, size = 28, object = 3
			 type = <class 'int'>, size = 28, object = 5
			 type = <class 'int'>, size = 28, object = 1
			 type = <class 'int'>, size = 28, object = 7
			 type = <class 'int'>, size = 28, object = 4
			 
Вывод:
В данном примере показано, что каждый объект списка затрачивает 28 байт памяти, также сам список затраичвает 192 байта,
если сравнивать со словарем то сам словарь затрачивает на себя 240 байт, не считая его элементов.
"""

