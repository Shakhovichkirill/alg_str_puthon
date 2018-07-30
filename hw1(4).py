# Задание №1

# Определить, какое число в массиве встречается чаще всего.

import random
def num():
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

# timeit
# 100 loops, best of 5: 29.9 nsec per loop
# 1000 loops, best of 5: 26.5 nsec per loop
# 10000 loops, best of 5: 26.9 nsec per loop

#cProfile.run("num()")
# 134 function calls in 0.001 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        20    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        20    0.000    0.000    0.000    0.000 random.py:218(randint)
#        20    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.001    0.001 test.py:4(num)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        20    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        28    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.Сами минимальный и максимальный элементы в сумму не включать.
def num_new():
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
    print(
        f'В массиве {list_n}, максимальное число {list_n[max_]}, минимальное число {list_n[min_]}, сумма элементов между этими числами {s}')

# timeit
# 100 loops, best of 5: 29.9 nsec per loop
# 1000 loops, best of 5: 49.2 nsec per loop
# 10000 loops, best of 5: 30 nsec per loop

#cProfile.run("num_new()")
# 73 function calls in 0.001 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        10    0.000    0.000    0.000    0.000 random.py:174(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:218(randint)
#        10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 test.py:4(num_new)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        18    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}